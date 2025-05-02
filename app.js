const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('userInput');
const typingIndicator = document.getElementById('typingIndicator');
const svg = d3.select("#memoryMap");

const net = new brain.recurrent.LSTM();

let trainingData = loadMemory() || [
  { input: "hello", output: "hi there!" },
  { input: "how are you", output: "i'm fine, thanks!" },
  { input: "what is your name", output: "i'm cleverbot." },
  { input: "dog", output: "barks" },
  { input: "cat", output: "meows" },
  { input: "sky", output: "blue" },
  { input: "grass", output: "green" },
  { input: "fire", output: "hot" },
  { input: "ice", output: "cold" },
  { input: "water", output: "wet" },
  { input: "sun", output: "bright" },
  { input: "moon", output: "glows" },
  { input: "computer", output: "computes" },
  { input: "tree", output: "grows" },
  { input: "rain", output: "falls" },
  { input: "clouds", output: "float" },
  { input: "bird", output: "flies" },
  { input: "fish", output: "swims" },
  { input: "phone", output: "calls" },
  { input: "car", output: "drives" },
  { input: "bike", output: "rides" },
  { input: "flower", output: "blooms" },
  { input: "wind", output: "blows" }
];

net.train(trainingData, {
  iterations: 500,
  errorThresh: 0.009
});
// Helper: Clean text
function clean(text) {
  return text.toLowerCase().replace(/[^a-z0-9\s]/g, '').trim();
}

// Tokenize input into pairs and sequences
function tokenize(input) {
  const words = clean(input).split(/\s+/);
  const tokens = [];
  for (let i = 0; i < words.length - 1; i++) {
    tokens.push([words[i], words[i + 1]]);
  }
  if (words.length > 2) {
    for (let i = 0; i < words.length - 2; i++) {
      tokens.push([words[i] + " " + words[i+1], words[i+2]]);
    }
  }
  return tokens;
}

// Strengthen memory
function learn(tokens) {
  tokens.forEach(([key, value]) => {
    if (!brain[key]) brain[key] = {};
    if (!brain[key][value]) brain[key][value] = 0;
    brain[key][value] += 1;
  });
}

// Decay memory slightly
function decayBrain() {
  for (let key in brain) {
    for (let val in brain[key]) {
      brain[key][val] *= 0.999;
      if (brain[key][val] < 0.5) {
        delete brain[key][val];
      }
    }
    if (Object.keys(brain[key]).length === 0) {
      delete brain[key];
    }
  }
}

// Predict next word(s)
function predict(lastInput) {
  const words = clean(lastInput).split(/\s+/);
  const last = words.slice(-2).join(" ") || words.slice(-1)[0];
  if (brain[last]) {
    const options = Object.entries(brain[last]);
    options.sort((a,b) => b[1]-a[1]);
    if (options.length > 0) {
      return options[0][0];
    }
  }
  return "";
}
function sendInput() {
  const input = userInput.value.trim();
  if (!input) return;

  addMessage('You', input);
  userInput.value = '';

  showTyping();

  setTimeout(() => {
    const tokens = tokenize(input);
    if (tokens.length >= 2) {
      for (let i = 0; i < tokens.length - 1; i++) {
        trainingData.push({ input: tokens[i], output: tokens[i + 1] });
      }
    }

    const output = net.run(input.toLowerCase()) || generateResponse(input);
    addMessage('Bot', output);

    net.train(trainingData, { iterations: 100, errorThresh: 0.02 });
    saveMemory();
    hideTyping();
    drawGraph();
  }, 800);
}

function addMessage(sender, message) {
  const msg = document.createElement('div');
  msg.className = "mb-2";
  msg.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatbox.appendChild(msg);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function showTyping() {
  typingIndicator.classList.remove('hidden');
}

function hideTyping() {
  typingIndicator.classList.add('hidden');
}

// Decay manual button
function decayButton() {
  decayBrain();
  alert('Memory slightly decayed!');
}
function generateResponse(input) {
  const responses = [
    "Interesting!",
    "I see.",
    "Can you explain that?",
    "Go on...",
    "Why do you say that?"
  ];
  return responses[Math.floor(Math.random() * responses.length)];
}

function saveMemory() {
  localStorage.setItem('cleverbotTrainingData', JSON.stringify(trainingData));
}
// 💾 Save the current brain
function saveBrain() {
  const memory = JSON.stringify(trainingData, null, 2);
  const blob = new Blob([memory], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  
  const a = document.createElement("a");
  a.href = url;
  a.download = "cleverbot_brain.json";
  a.click();
  
  URL.revokeObjectURL(url);
}

// 📂 Load a brain from a file
function loadBrain(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function(e) {
    try {
      const loadedData = JSON.parse(e.target.result);
      if (Array.isArray(loadedData)) {
        trainingData = loadedData;
        net.train(trainingData, { iterations: 500, errorThresh: 0.009 });
        saveMemory(); // Also update localStorage
        drawGraph();  // Redraw the memory map
        alert('Brain loaded successfully!');
      } else {
        alert('Invalid brain file.');
      }
    } catch (err) {
      alert('Error loading brain: ' + err.message);
    }
  };
  reader.readAsText(file);
}

function loadMemory() {
  const data = localStorage.getItem('cleverbotTrainingData');
  return data ? JSON.parse(data) : null;
}

// 🧠 GRAPH DRAWING SECTION
function drawGraph() {
  svg.selectAll("*").remove(); // clear previous

  const nodes = [];
  const links = [];

  const nodeMap = {};

  trainingData.forEach(pair => {
    if (!nodeMap[pair.input]) {
      nodeMap[pair.input] = { id: pair.input };
      nodes.push(nodeMap[pair.input]);
    }
    if (!nodeMap[pair.output]) {
      nodeMap[pair.output] = { id: pair.output };
      nodes.push(nodeMap[pair.output]);
    }
    links.push({ source: pair.input, target: pair.output });
  });

  const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(80))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(svg.node().clientWidth / 2, svg.node().clientHeight / 2));

  const link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(links)
    .join("line")
      .attr("stroke-width", 1.5);

  const node = svg.append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
    .selectAll("circle")
    .data(nodes)
    .join("circle")
      .attr("r", 10)
      .attr("fill", "#6366f1")
      .call(drag(simulation));

  const label = svg.append("g")
    .selectAll("text")
    .data(nodes)
    .join("text")
      .text(d => d.id)
      .attr("font-size", 10)
      .attr("fill", "#333");

  simulation.on("tick", () => {
    link
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);

    node
      .attr("cx", d => d.x)
      .attr("cy", d => d.y);

    label
      .attr("x", d => d.x + 12)
      .attr("y", d => d.y + 4);
  });
}

function drag(simulation) {
  function dragstarted(event) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  }

  function dragged(event) {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
  }

  function dragended(event) {
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
  }

  return d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended);
}

// Initialize the first graph
drawGraph();
