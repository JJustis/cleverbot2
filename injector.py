#!/usr/bin/env python3
"""
Meta-Cognition Injector for Enhanced Cleverbot

This script injects a meta-cognition layer into the Cleverbot system,
enabling the bot to recursively analyze its own thinking process and
improve response quality over time.

Usage:
    python fixed_injector.py --backup --inject

"""

import os
import sys
import json
import re
import argparse
import shutil
from datetime import datetime

class MetaCognitionInjector:
    def __init__(self, backup=True):
        self.backup = backup
        self.files = {
            'index': 'index.html',
            'getdata': 'getmodeldata.php',
            'savedata': 'savemodeldata.php'
        }
        self.backup_dir = 'backup_' + datetime.now().strftime('%Y%m%d_%H%M%S')
        
    def create_backup(self):
        """Create backup of original files"""
        if not self.backup:
            return
            
        print(f"Creating backup in {self.backup_dir}...")
        os.makedirs(self.backup_dir, exist_ok=True)
        
        for file_key, filename in self.files.items():
            if os.path.exists(filename):
                shutil.copy2(filename, os.path.join(self.backup_dir, filename))
                print(f"Backed up {filename}")
                
        print("Backup complete")
    
    def inject_meta_cognition(self):
        """Inject meta-cognition components into the system"""
        print("Injecting meta-cognition layer...")
        
        # Modify index.html
        if os.path.exists(self.files['index']):
            self._inject_into_index()
        else:
            print(f"Warning: {self.files['index']} not found")
            
        # Modify getmodeldata.php to support meta-cognition data
        if os.path.exists(self.files['getdata']):
            self._inject_into_getdata()
        else:
            print(f"Warning: {self.files['getdata']} not found")
            
        # Modify savemodeldata.php to save meta-cognition data
        if os.path.exists(self.files['savedata']):
            self._inject_into_savedata()
        else:
            print(f"Warning: {self.files['savedata']} not found")
            
        print("Meta-cognition layer injection complete!")
        
    def _inject_into_index(self):
        """Inject meta-cognition code into index.html"""
        try:
            with open(self.files['index'], 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Add meta-cognition UI elements
            meta_ui = """
  <div class="mt-4 p-4 border rounded-xl bg-gradient-to-r from-purple-100 to-indigo-100">
    <h3 class="font-semibold text-purple-700 mb-2">Meta-Cognition System</h3>
    <div class="flex flex-col gap-2">
      <div class="flex justify-between">
        <div class="text-sm text-purple-700">Self-Reflection Depth: <span id="reflectionLevel">3</span></div>
        <div class="flex gap-2">
          <button id="toggleMetaCognition" class="bg-purple-200 text-purple-700 px-3 py-1 rounded-lg hover:bg-purple-300 transition">
            Enable Meta-Cognition
          </button>
          <button id="analyzePerformance" class="bg-indigo-200 text-indigo-700 px-3 py-1 rounded-lg hover:bg-indigo-300 transition">
            Analyze Performance
          </button>
        </div>
      </div>
      <div class="mt-2">
        <div class="w-full bg-gray-200 rounded-full h-2.5">
          <div class="bg-purple-600 h-2.5 rounded-full" id="metaCognitionProgress" style="width: 25%"></div>
        </div>
      </div>
      <div id="metaCognitionInsights" class="text-xs text-gray-700 mt-1 h-24 overflow-y-auto bg-white p-2 rounded">
        Meta-cognition system ready. Enable to activate enhanced recursive thinking capabilities.
      </div>
    </div>
  </div>"""
            
            # Insert after the last div before </body>
            pattern = r'(</div>\s*</div>\s*</div>\s*<script>)'
            replacement = meta_ui + r'\n\1'
            content = re.sub(pattern, replacement, content)
            
            # Insert meta-cognition JavaScript class and main code
            meta_js = self._get_meta_cognition_js()
            
            # Add the code before the closing </body> tag
            content = content.replace('</body>', f'{meta_js}\n</body>')
            
            # Write the modified content
            with open(self.files['index'], 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Successfully injected meta-cognition UI and code into {self.files['index']}")
            
        except Exception as e:
            print(f"Error injecting into {self.files['index']}: {e}")
    
    def _get_meta_cognition_js(self):
        """Return JavaScript code for meta-cognition system"""
        return """
<script>
// Meta-Cognition System for Enhanced Cleverbot
class MetaCognitionSystem {
  constructor() {
    this.enabled = false;
    this.reflectionLevel = 3;
    this.responseHistory = [];
    this.maxHistorySize = 100;
    this.insightPatterns = new Map();
    this.performanceMetrics = {
      coherence: 0,
      diversity: 0,
      relevance: 0,
      depth: 0,
      learning: 0
    };
    this.reflectionThreshold = 0.7;
    this.lastAnalysisTime = Date.now();
    this.selfImprovementLog = [];
    this.recursionLimiter = {
      maxDepth: 5,
      currentDepth: 0,
      timeout: 2000 // ms
    };
    this.conceptualModels = new Map();
    this.thinkingTrace = [];
    this.metaPatterns = [];
    this.insightCounter = 0;
  }
  
  // Initialize the meta-cognition system
  initialize() {
    console.log("Initializing Meta-Cognition System...");
    this._setupEventListeners();
    this._loadMetaCognitionData();
    this._updateUIState();
    
    // Start periodic self-reflection
    setInterval(() => this._periodicSelfReflection(), 60000); // Every minute
    
    return this;
  }
  
  // Set up UI event listeners
  _setupEventListeners() {
    const toggleBtn = document.getElementById('toggleMetaCognition');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        this.enabled = !this.enabled;
        this._updateUIState();
        this._logSystemEvent(this.enabled ? 'Meta-cognition enabled' : 'Meta-cognition disabled');
      });
    }
    
    const analyzeBtn = document.getElementById('analyzePerformance');
    if (analyzeBtn) {
      analyzeBtn.addEventListener('click', () => {
        this.analyzeSystemPerformance();
      });
    }
  }
  
  // Update UI based on current state
  _updateUIState() {
    const toggleBtn = document.getElementById('toggleMetaCognition');
    const progressBar = document.getElementById('metaCognitionProgress');
    const insights = document.getElementById('metaCognitionInsights');
    const reflectionLevel = document.getElementById('reflectionLevel');
    
    if (toggleBtn) {
      toggleBtn.textContent = this.enabled ? 'Disable Meta-Cognition' : 'Enable Meta-Cognition';
      toggleBtn.className = this.enabled 
        ? 'bg-purple-500 text-white px-3 py-1 rounded-lg hover:bg-purple-600 transition'
        : 'bg-purple-200 text-purple-700 px-3 py-1 rounded-lg hover:bg-purple-300 transition';
    }
    
    if (progressBar) {
      // Calculate overall system performance
      const overallPerformance = Object.values(this.performanceMetrics).reduce((sum, val) => sum + val, 0) / 
                                  Object.keys(this.performanceMetrics).length;
      progressBar.style.width = `${Math.round(overallPerformance * 100)}%`;
    }
    
    if (reflectionLevel) {
      reflectionLevel.textContent = this.reflectionLevel;
    }
    
    if (insights && this.selfImprovementLog.length > 0) {
      insights.innerHTML = this.selfImprovementLog.slice(-5).map(entry => 
        `<div class="text-xs mb-1">${entry}</div>`
      ).join('');
    }
  }
  
  // Load previously saved meta-cognition data
  async _loadMetaCognitionData() {
    try {
      const metaData = localStorage.getItem('cleverbotMetaCognition');
      if (metaData) {
        const parsedData = JSON.parse(metaData);
        
        // Restore from saved data
        this.insightPatterns = new Map(parsedData.insightPatterns || []);
        this.responseHistory = parsedData.responseHistory || [];
        this.performanceMetrics = parsedData.performanceMetrics || this.performanceMetrics;
        this.selfImprovementLog = parsedData.selfImprovementLog || [];
        this.metaPatterns = parsedData.metaPatterns || [];
        
        // Log successful loading
        this._logSystemEvent(`Loaded ${this.responseHistory.length} historical responses and ${this.insightPatterns.size} patterns`);
      }
    } catch (error) {
      console.error('Error loading meta-cognition data:', error);
      this._logSystemEvent(`Error loading meta-cognition data: ${error.message}`);
    }
  }
  
  // Save current meta-cognition state
  _saveMetaCognitionData() {
    try {
      const dataToSave = {
        insightPatterns: Array.from(this.insightPatterns.entries()),
        responseHistory: this.responseHistory.slice(-this.maxHistorySize),
        performanceMetrics: this.performanceMetrics,
        selfImprovementLog: this.selfImprovementLog.slice(-50),
        metaPatterns: this.metaPatterns.slice(-50),
        lastSaved: Date.now()
      };
      
      localStorage.setItem('cleverbotMetaCognition', JSON.stringify(dataToSave));
    } catch (error) {
      console.error('Error saving meta-cognition data:', error);
    }
  }
  
  // Process an input-response pair through meta-cognition system
  processInteraction(input, response, responseSource) {
    if (!this.enabled) return response;
    
    // Add to response history
    this.responseHistory.push({
      timestamp: Date.now(),
      input,
      response,
      responseSource,
      evaluation: null
    });
    
    // Keep history within limit
    if (this.responseHistory.length > this.maxHistorySize) {
      this.responseHistory.shift();
    }
    
    // Perform recursive thinking on response
    const enhancedResponse = this._performRecursiveThinking(input, response);
    
    // Update metrics
    this._updateResponseMetrics(input, enhancedResponse);
    
    // Save updated state
    this._saveMetaCognitionData();
    
    return enhancedResponse;
  }
  
  // Main recursive thinking method
  _performRecursiveThinking(input, response) {
    // Reset recursion limiter
    this.recursionLimiter.currentDepth = 0;
    this.thinkingTrace = [];
    
    // Begin recursive thinking process
    return this._recursiveThoughtStep(input, response, "initial");
  }
  
  // Single recursive thought step
  _recursiveThoughtStep(input, currentResponse, stage) {
    // Check recursion limits
    if (this.recursionLimiter.currentDepth >= this.recursionLimiter.maxDepth) {
      this._logSystemEvent(`Recursion depth limit reached (${this.recursionLimiter.maxDepth})`);
      return currentResponse;
    }
    
    // Increment recursion depth counter
    this.recursionLimiter.currentDepth++;
    
    // Track thinking stages
    this.thinkingTrace.push({
      depth: this.recursionLimiter.currentDepth,
      stage,
      response: currentResponse
    });
    
    // Apply different types of recursive thinking based on current depth
    let enhancedResponse = currentResponse;
    
    switch (this.recursionLimiter.currentDepth) {
      case 1:
        // First level: Context and relevance refinement
        enhancedResponse = this._improveRelevance(input, currentResponse);
        return this._recursiveThoughtStep(input, enhancedResponse, "relevance");
        
      case 2:
        // Second level: Coherence and structure enhancement
        enhancedResponse = this._improveCoherence(input, currentResponse);
        return this._recursiveThoughtStep(input, enhancedResponse, "coherence");
        
      case 3:
        // Third level: Diversity and creativity enhancement
        enhancedResponse = this._improveDiversity(input, currentResponse);
        
        // Only continue to deeper reflection if needed based on complexity
        if (this._needsDeeperReflection(input)) {
          return this._recursiveThoughtStep(input, enhancedResponse, "diversity");
        }
        return enhancedResponse;
        
      case 4:
        // Fourth level: Deep conceptual refinement
        enhancedResponse = this._improveConceptualDepth(input, currentResponse);
        return this._recursiveThoughtStep(input, enhancedResponse, "depth");
        
      case 5:
        // Final level: Meta-pattern analysis and innovation
        enhancedResponse = this._improveWithMetaPatterns(input, currentResponse);
        
        // Log insight from deep reflection
        if (enhancedResponse !== currentResponse) {
          this.insightCounter++;
          this._logSystemEvent(`Insight #${this.insightCounter}: Deep meta-reflection transformed response`);
        }
        return enhancedResponse;
        
      default:
        return currentResponse;
    }
  }
  
  // Determine if input requires deeper reflection levels
  _needsDeeperReflection(input) {
    // Check if input contains complex questions or topics
    const complexityIndicators = [
      'why', 'how', 'explain', 'understand', 'meaning', 'purpose',
      'difference', 'compare', 'relation', 'between', 'philosophy',
      'concept', 'theory', 'define', 'ethical', 'moral'
    ];
    
    const inputLower = input.toLowerCase();
    const hasComplexityIndicator = complexityIndicators.some(word => inputLower.includes(word));
    
    // Check input length as a complexity proxy
    const isLongInput = input.split(' ').length > 8;
    
    // Check if we have relevant meta-patterns
    const hasRelevantPatterns = this.metaPatterns.some(pattern => 
      pattern.keywords.some(keyword => inputLower.includes(keyword))
    );
    
    return (hasComplexityIndicator && isLongInput) || hasRelevantPatterns;
  }
  
  // Enhance response relevance to input
  _improveRelevance(input, response) {
    // Skip enhancement if response is already excellent
    if (this._evaluateResponseQuality(input, response) > this.reflectionThreshold) {
      return response;
    }
    
    // Get key concepts from input and response
    const inputConcepts = this._extractKeyConcepts(input);
    const responseConcepts = this._extractKeyConcepts(response);
    
    // Find missing key concepts
    const missingConcepts = inputConcepts.filter(concept => 
      !responseConcepts.some(respConcept => respConcept.includes(concept) || concept.includes(respConcept))
    );
    
    // If no significant concepts are missing, return original
    if (missingConcepts.length === 0) {
      return response;
    }
    
    // Attempt to incorporate missing concepts
    let enhancedResponse = response;
    
    // Simple enhancement: Add reference to missing concepts
    if (missingConcepts.length > 0) {
      // Look for relevant patterns in history to handle these concepts
      const relevantPatterns = this._findRelevantPatterns(missingConcepts);
      
      if (relevantPatterns.length > 0) {
        // Use pattern to enhance response
        const pattern = relevantPatterns[0];
        enhancedResponse = this._applyResponsePattern(response, pattern, missingConcepts);
      } else {
        // Simple addition if no patterns available
        const missingConceptsText = missingConcepts.join(', ');
        
        // Avoid simply appending to prevent awkward responses
        // Instead, look for good insertion points or sentence reformulation
        if (response.includes('.')) {
          // Insert before last sentence
          const sentences = response.split('.');
          if (sentences.length > 1) {
            sentences.splice(sentences.length - 1, 0, 
              ` I should also address ${missingConceptsText}`);
            enhancedResponse = sentences.join('.');
          }
        } else {
          // For short responses, consider the context more carefully
          enhancedResponse = `${response} Regarding ${missingConceptsText}, it's also worth considering.`;
        }
      }
    }
    
    return enhancedResponse;
  }
  
  // Enhance response coherence
  _improveCoherence(input, response) {
    // Basic coherence checks
    const sentences = response.split(/[.!?]+/).filter(s => s.trim().length > 0);
    
    // Skip if response is very short or already coherent
    if (sentences.length <= 1) {
      return response;
    }
    
    // Check for abrupt transitions between sentences
    let enhancedResponse = response;
    let hasImprovements = false;
    
    for (let i = 1; i < sentences.length; i++) {
      const prevSentence = sentences[i-1].trim();
      const currentSentence = sentences[i].trim();
      
      // Skip if either sentence is too short
      if (prevSentence.split(' ').length < 3 || currentSentence.split(' ').length < 3) {
        continue;
      }
      
      // Check for semantic connection between adjacent sentences
      const prevConcepts = this._extractKeyConcepts(prevSentence);
      const currentConcepts = this._extractKeyConcepts(currentSentence);
      
      // Check concept overlap
      const hasConceptOverlap = prevConcepts.some(c1 => 
        currentConcepts.some(c2 => c1.includes(c2) || c2.includes(c1))
      );
      
      if (!hasConceptOverlap) {
        // Find transition phrases appropriate for the context
        const transition = this._selectTransitionPhrase(prevSentence, currentSentence);
        
        // Apply transition
        enhancedResponse = enhancedResponse.replace(
          `${prevSentence}. ${currentSentence}`, 
          `${prevSentence}. ${transition} ${currentSentence}`
        );
        
        hasImprovements = true;
      }
    }
    
    // Check for structural improvement opportunity
    if (!hasImprovements && sentences.length >= 3) {
      // Consider restructuring for clarity if sentences share concepts but order seems random
      const allConcepts = sentences.flatMap(s => this._extractKeyConcepts(s));
      const conceptFrequency = allConcepts.reduce((acc, concept) => {
        acc[concept] = (acc[concept] || 0) + 1;
        return acc;
      }, {});
      
      // Find recurring concepts that could form a thematic structure
      const recurringConcepts = Object.entries(conceptFrequency)
        .filter(([_, count]) => count > 1)
        .map(([concept, _]) => concept);
      
      if (recurringConcepts.length > 0) {
        // Log structural improvement
        this._logSystemEvent(`Improved response coherence around concepts: ${recurringConcepts.slice(0, 3).join(', ')}`);
      }
    }
    
    return enhancedResponse;
  }
  
  // Enhance response diversity
  _improveDiversity(input, response) {
    // Compare with recent responses to check for repetitiveness
    const recentResponses = this.responseHistory
      .slice(-10)
      .filter(item => item.response !== response)
      .map(item => item.response);
    
    if (recentResponses.length === 0) {
      return response; // No comparison data
    }
    
    // Check for repeated phrases or patterns
    const responsePhrases = response.split(/[.!?]/).filter(s => s.trim().length > 0);
    let hasRepetitivePatterns = false;
    
    for (const phrase of responsePhrases) {
      if (phrase.split(' ').length < 4) continue; // Skip very short phrases
      
      // Check if similar phrases appear in recent responses
      const similarity = recentResponses.some(recentResp => 
        recentResp.includes(phrase) || this._calculateSimilarity(phrase, recentResp) > 0.7
      );
      
      if (similarity) {
        hasRepetitivePatterns = true;
        break;
      }
    }
    
    if (!hasRepetitivePatterns) {
      return response; // No need to improve diversity
    }
    
    // If repetitive patterns found, attempt to diversify
    // Extract key elements and rephrase them
    const inputConcepts = this._extractKeyConcepts(input);
    let enhancedResponse = response;
    
    // Find alternative expressions for repeated concepts
    const conceptAlternatives = this._generateConceptAlternatives(inputConcepts);
    
    // Apply alternatives to diversify
    for (const [concept, alternatives] of Object.entries(conceptAlternatives)) {
      if (alternatives.length === 0) continue;
      
      // Select an alternative that hasn't been used recently
      const unused = alternatives.find(alt => 
        !recentResponses.some(recentResp => recentResp.includes(alt))
      ) || alternatives[0];
      
      // Replace concept with alternative, being careful about word boundaries
      const conceptRegex = new RegExp(`\\b${concept}\\b`, 'gi');
      enhancedResponse = enhancedResponse.replace(conceptRegex, unused);
    }
    
    // Log diversity improvement
    if (enhancedResponse !== response) {
      this._logSystemEvent('Improved response diversity by varying concept expressions');
    }
    
    return enhancedResponse;
  }
  
  // Enhance response with deeper conceptual understanding
  _improveConceptualDepth(input, response) {
    // Check if input contains deep questions or abstract topics
    const inputLower = input.toLowerCase();
    const abstractTopics = [
      'philosophy', 'consciousness', 'meaning', 'purpose', 'ethics',
      'morality', 'existence', 'reality', 'truth', 'knowledge',
      'being', 'identity', 'nature', 'universe', 'concept'
    ];
    
    const hasAbstractTopic = abstractTopics.some(topic => inputLower.includes(topic));
    
    if (!hasAbstractTopic) {
      return response; // No need for deeper conceptual analysis
    }
    
    // Extract key abstract concepts from input
    const abstractConcepts = abstractTopics.filter(topic => inputLower.includes(topic));
    
    // Check if we have conceptual models for these topics
    const relevantModels = abstractConcepts.filter(concept => this.conceptualModels.has(concept));
    
    if (relevantModels.length === 0) {
      // No existing models, create a basic conceptual model from the response
      for (const concept of abstractConcepts) {
        this.conceptualModels.set(concept, {
          relatedConcepts: this._extractKeyConcepts(response),
          perspectives: [response],
          lastUpdated: Date.now()
        });
      }
      
      // Log model creation
      this._logSystemEvent(`Created initial conceptual models for: ${abstractConcepts.join(', ')}`);
      return response;
    }
    
    // We have relevant models, enhance response with deeper perspectives
    let enhancedResponse = response;
    const mainConcept = relevantModels[0]; // Focus on primary concept
    const model = this.conceptualModels.get(mainConcept);
    
    // Generate a more nuanced response based on conceptual model
    if (model.perspectives.length > 1) {
      // Multiple perspectives available, integrate a secondary viewpoint
      const existingPerspective = model.perspectives.find(p => response.includes(p));
      const alternativePerspectives = model.perspectives.filter(p => p !== existingPerspective);
      
      if (alternativePerspectives.length > 0) {
        // Select a complementary perspective
        const altPerspective = alternativePerspectives[0];
        
        // Integrate the alternative perspective
        if (enhancedResponse.includes('.')) {
          const sentences = enhancedResponse.split('.');
          sentences.splice(sentences.length - 1, 0, 
            ` Another way to view ${mainConcept} is ${altPerspective}`);
          enhancedResponse = sentences.join('.');
        } else {
          enhancedResponse += ` Another way to think about ${mainConcept} is ${altPerspective}`;
        }
        
        // Log conceptual enhancement
        this._logSystemEvent(`Enhanced response with deeper conceptual perspective on ${mainConcept}`);
      }
    }
    
    // Update the conceptual model with the current interaction
    model.relatedConcepts = [...new Set([...model.relatedConcepts, ...this._extractKeyConcepts(input)])];
    if (!model.perspectives.includes(response)) {
      model.perspectives.push(response);
    }
    model.lastUpdated = Date.now();
    this.conceptualModels.set(mainConcept, model);
    
    return enhancedResponse;
  }
  
  // Apply meta-pattern improvements
  _improveWithMetaPatterns(input, response) {
    // Skip if no meta-patterns available
    if (this.metaPatterns.length === 0) {
      return response;
    }
    
    const inputConcepts = this._extractKeyConcepts(input);
    
    // Find relevant meta-patterns
    const relevantPatterns = this.metaPatterns.filter(pattern => 
      pattern.keywords.some(keyword => 
        inputConcepts.some(concept => concept.includes(keyword) || keyword.includes(concept))
      )
    );
    
    if (relevantPatterns.length === 0) {
      return response;
    }
    
    // Apply most relevant meta-pattern
    const topPattern = relevantPatterns[0];
    
    // Different application strategies based on pattern type
    switch (topPattern.type) {
      case 'question-reframe':
        if (!response.includes('?')) {
          // Transform part of response into a question to deepen thinking
          return this._transformToReflectiveQuestion(response, topPattern);
        }
        break;
        
      case 'perspective-shift':
        // Add alternative perspective
        return this._addAlternativePerspective(response, topPattern);
        
      case 'concept-elaboration':
        // Elaborate on core concept
        return this._elaborateOnConcept(response, inputConcepts, topPattern);
        
      case 'implicit-insight':
        // Add implicit insight
        return this._addImplicitInsight(response, topPattern);
    }
    
    return response;
  }
  
  // Transform response to include reflective question
  _transformToReflectiveQuestion(response, pattern) {
    // Split into sentences
    const sentences = response.split(/[.!?]/).filter(s => s.trim().length > 0);
    
    // Skip if too short
    if (sentences.length < 2) return response;
    
    // Get key concepts to question about
    const concepts = this._extractKeyConcepts(response);
    if (concepts.length === 0) return response;
    
    // Select a concept to question
    const conceptToQuestion = concepts[0];
    
    // Create reflective question
    const questionTemplates = [
      `Have you considered how ${conceptToQuestion} might relate to wider contexts?`,
      `What implications might ${conceptToQuestion} have beyond what we've discussed?`,
      `How does your understanding of ${conceptToQuestion} influence your perspective?`,
      `What further questions does this raise about ${conceptToQuestion}?`
    ];
    
    const question = questionTemplates[Math.floor(Math.random() * questionTemplates.length)];
    
    // Add question to end of response
    return response + ` ${question}`;
  }
  
  // Add alternative perspective to response
  _addAlternativePerspective(response, pattern) {
    const transitions = [
      "From another perspective,",
      "Alternatively,",
      "Looking at this differently,",
      "Another way to see this is",
      "A different viewpoint suggests"
    ];
    
    const transition = transitions[Math.floor(Math.random() * transitions.length)];
    const perspective = pattern.templates[Math.floor(Math.random() * pattern.templates.length)];
    
    // Add to end or as new paragraph
    if (response.includes('.')) {
      const sentences = response.split('.');
      sentences.splice(sentences.length - 1, 0, ` ${transition} ${perspective}`);
      return sentences.join('.');
    }
    
    return `${response} ${transition} ${perspective}`;
  }
  
  // Elaborate on key concept
  _elaborateOnConcept(response, concepts, pattern) {
    if (concepts.length === 0) return response;
    
    const concept = concepts[0];
    const elaboration = pattern.templates[Math.floor(Math.random() * pattern.templates.length)]
      .replace('{{concept}}', concept);
    
    // Find good place to insert elaboration
    if (response.includes(concept) && response.includes('.')) {
      // Insert after sentence containing the concept
      const sentences = response.split('.');
      for (let i = 0; i < sentences.length; i++) {
        if (sentences[i].includes(concept)) {sentences.splice(i + 1, 0, ` ${elaboration}`);
          return sentences.join('.');
        }
      }
    }
    
    // Fallback: append to response
    return `${response} ${elaboration}`;
  }
  
  // Add an implicit insight that connects ideas in a new way
  _addImplicitInsight(response, pattern) {
    const insights = pattern.templates;
    const insight = insights[Math.floor(Math.random() * insights.length)];
    
    // Add insight as a final thought
    if (response.includes('.')) {
      return response + ` ${insight}`;
    }
    
    return `${response}. ${insight}`;
  }
  
  // Extract key concepts from text
  _extractKeyConcepts(text) {
    // Simple concept extraction based on word frequency and importance
    const words = text.toLowerCase()
      .replace(/[^\w\s]/g, ' ')
      .split(/\s+/)
      .filter(w => w.length > 3);
      
    // Filter out common stop words
    const stopWords = ["this", "that", "these", "those", "there", "their", "they", "have", 
                      "with", "from", "about", "some", "what", "when", "where", "which"];
    
    const filteredWords = words.filter(word => !stopWords.includes(word));
    
    // Count word frequencies
    const wordCounts = {};
    filteredWords.forEach(word => {
      wordCounts[word] = (wordCounts[word] || 0) + 1;
    });
    
    // Get top concepts (most frequent meaningful words)
    return Object.entries(wordCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([word]) => word);
  }
  
  // Select appropriate transition phrase based on context
  _selectTransitionPhrase(sentence1, sentence2) {
    // Analyze relationship between sentences
    const s1Concepts = this._extractKeyConcepts(sentence1);
    const s2Concepts = this._extractKeyConcepts(sentence2);
    
    // Check for contrast
    const contrastIndicators = ["but", "however", "though", "although", "contrary"];
    const s2Lower = sentence2.toLowerCase();
    const hasContrast = contrastIndicators.some(word => s2Lower.includes(word));
    
    // Simple transition selection
    if (hasContrast) {
      return "However,";
    }
    
    // Check for elaboration or example
    if (s1Concepts.some(c => s2Concepts.includes(c))) {
      const transitions = ["For example,", "Specifically,", "In particular,", "To elaborate,"];
      return transitions[Math.floor(Math.random() * transitions.length)];
    }
    
    // Default transitional phrases
    const defaultTransitions = [
      "Additionally,", "Furthermore,", "Moreover,", "Also,", "What's more,", 
      "Building on this,", "In relation to this,"
    ];
    
    return defaultTransitions[Math.floor(Math.random() * defaultTransitions.length)];
  }
  
  // Find relevant response patterns for given concepts
  _findRelevantPatterns(concepts) {
    const patterns = [];
    
    // Check each stored pattern for relevance
    for (const [patternKey, pattern] of this.insightPatterns.entries()) {
      // Check if pattern concepts overlap with our target concepts
      const patternConcepts = patternKey.split('|');
      const overlap = patternConcepts.filter(pc => 
        concepts.some(c => c.includes(pc) || pc.includes(c))
      );
      
      if (overlap.length > 0) {
        patterns.push({
          key: patternKey,
          pattern,
          relevance: overlap.length / Math.max(patternConcepts.length, concepts.length)
        });
      }
    }
    
    // Sort by relevance
    return patterns.sort((a, b) => b.relevance - a.relevance);
  }
  
  // Apply a response pattern to enhance a response
  _applyResponsePattern(response, patternData, concepts) {
    const { pattern } = patternData;
    
    // Skip if no template available
    if (!pattern.template) {
      return response;
    }
    
    // Replace placeholders in template
    let enhancedText = pattern.template;
    
    // Replace {{concept}} with appropriate concept
    if (enhancedText.includes('{{concept}}') && concepts.length > 0) {
      enhancedText = enhancedText.replace(/{{concept}}/g, concepts[0]);
    }
    
    // Integrate with original response
    if (response.includes('.')) {
      // Add after a sentence break
      const sentences = response.split('.');
      sentences.splice(sentences.length - 1, 0, ` ${enhancedText}`);
      return sentences.join('.');
    }
    
    // For short responses, append with appropriate connection
    return `${response}. ${enhancedText}`;
  }
  
  // Generate alternatives for concepts to increase diversity
  _generateConceptAlternatives(concepts) {
    const alternatives = {};
    
    for (const concept of concepts) {
      // Skip very short concepts
      if (concept.length < 4) continue;
      
      alternatives[concept] = [];
      
      // Check for synonyms or related terms in semantic network
      if (window.advancedEngine && window.advancedEngine.semanticNetwork) {
        // Get related words from semantic network
        const semanticNode = window.advancedEngine.semanticNetwork.get(concept);
        if (semanticNode && semanticNode.associations) {
          const relatedTerms = Array.from(semanticNode.associations.keys())
            .slice(0, 3);
          alternatives[concept].push(...relatedTerms);
        }
      }
      
      // Check for alternatives from conceptual models
      if (this.conceptualModels.has(concept)) {
        const model = this.conceptualModels.get(concept);
        alternatives[concept].push(...model.relatedConcepts);
      }
      
      // Add simple variants using common modifiers
      alternatives[concept].push(`the ${concept}`);
      alternatives[concept].push(`this ${concept}`);
      alternatives[concept].push(`such ${concept}`);
      
      // Ensure uniqueness
      alternatives[concept] = [...new Set(alternatives[concept])];
    }
    
    return alternatives;
  }
  
  // Evaluate response quality based on multiple metrics
  _evaluateResponseQuality(input, response) {
    // Quick early return for very short inputs/responses
    if (input.length < 5 || response.length < 10) {
      return 0.5; // Neutral score for minimal content
    }
    
    // Multiple quality dimensions
    const metrics = {
      relevance: this._calculateRelevance(input, response),
      coherence: this._calculateCoherence(response),
      diversity: this._calculateDiversity(response),
      depth: response.length / 200 // Simple proxy for depth (max score at 200+ chars)
    };
    
    // Weighted average of metrics
    const weights = { relevance: 0.4, coherence: 0.3, diversity: 0.2, depth: 0.1 };
    let weightedSum = 0;
    let totalWeight = 0;
    
    for (const [metric, value] of Object.entries(metrics)) {
      weightedSum += value * weights[metric];
      totalWeight += weights[metric];
    }
    
    return weightedSum / totalWeight;
  }
  
  // Calculate relevance between input and response
  _calculateRelevance(input, response) {
    const inputConcepts = this._extractKeyConcepts(input);
    const responseConcepts = this._extractKeyConcepts(response);
    
    // No concepts found (too short)
    if (inputConcepts.length === 0 || responseConcepts.length === 0) {
      return 0.5;
    }
    
    // Count concept overlap
    let overlapCount = 0;
    for (const inConcept of inputConcepts) {
      for (const resConcept of responseConcepts) {
        if (inConcept.includes(resConcept) || resConcept.includes(inConcept)) {
          overlapCount++;
          break;
        }
      }
    }
    
    return overlapCount / inputConcepts.length;
  }
  
  // Calculate internal coherence of response
  _calculateCoherence(response) {
    // Split into sentences
    const sentences = response.split(/[.!?]/).filter(s => s.trim().length > 0);
    
    // Too short to evaluate coherence
    if (sentences.length <= 1) {
      return 0.8; // Assume coherent if just one sentence
    }
    
    // Check adjacent sentence similarity for abrupt transitions
    let coherenceScore = 0;
    for (let i = 1; i < sentences.length; i++) {
      const similarity = this._calculateSimilarity(sentences[i-1], sentences[i]);
      coherenceScore += similarity;
    }
    
    return coherenceScore / (sentences.length - 1);
  }
  
  // Calculate diversity compared to recent responses
  _calculateDiversity(response) {
    const recentResponses = this.responseHistory
      .slice(-5)
      .filter(item => item.response !== response)
      .map(item => item.response);
    
    if (recentResponses.length === 0) {
      return 1.0; // Max diversity if no comparison data
    }
    
    // Calculate similarity to recent responses
    let totalSimilarity = 0;
    for (const recentResp of recentResponses) {
      totalSimilarity += this._calculateSimilarity(response, recentResp);
    }
    
    const avgSimilarity = totalSimilarity / recentResponses.length;
    return 1.0 - avgSimilarity; // Convert similarity to diversity
  }
  
  // Calculate similarity between two texts
  _calculateSimilarity(text1, text2) {
    // Simple Jaccard similarity on words
    const words1 = new Set(text1.toLowerCase().split(/\s+/));
    const words2 = new Set(text2.toLowerCase().split(/\s+/));
    
    // Calculate intersection and union
    const intersection = new Set([...words1].filter(x => words2.has(x)));
    const union = new Set([...words1, ...words2]);
    
    return intersection.size / union.size;
  }
  
  // Update response metrics based on input/response pair
  _updateResponseMetrics(input, response) {
    // Update performance metrics with exponential moving average
    const alpha = 0.2; // Smoothing factor
    const newMetrics = {
      coherence: this._calculateCoherence(response),
      diversity: this._calculateDiversity(response),
      relevance: this._calculateRelevance(input, response),
      depth: Math.min(1.0, response.length / 200),
      // Learning is based on growth of patterns and insights
      learning: Math.min(1.0, (this.insightPatterns.size + this.metaPatterns.length) / 100)
    };
    
    // Update each metric
    for (const [metric, value] of Object.entries(newMetrics)) {
      this.performanceMetrics[metric] = alpha * value + (1 - alpha) * this.performanceMetrics[metric];
    }
    
    // Update UI
    this._updateUIState();
  }
  
  // Perform periodic self-reflection
  _periodicSelfReflection() {
    if (!this.enabled) return;
    
    // Skip if last analysis was recent
    const timeSinceLastAnalysis = Date.now() - this.lastAnalysisTime;
    if (timeSinceLastAnalysis < 60000) return; // At least 1 minute between reflections
    
    // Need sufficient data for meaningful reflection
    if (this.responseHistory.length < 5) return;
    
    this.lastAnalysisTime = Date.now();
    
    // Identify patterns and insights
    this._identifyResponsePatterns();
    this._identifyMetaPatterns();
    
    // Log self-reflection event
    this._logSystemEvent(`Self-reflection complete. ${this.insightPatterns.size} patterns, ${this.metaPatterns.length} meta-patterns identified.`);
  }
  
  // Identify useful response patterns from history
  _identifyResponsePatterns() {
    // Need at least 5 interactions
    if (this.responseHistory.length < 5) return;
    
    // Get high-quality responses
    const qualityThreshold = 0.7;
    const goodResponses = this.responseHistory.filter(item => {
      // Calculate quality if not already evaluated
      if (item.evaluation === null) {
        item.evaluation = this._evaluateResponseQuality(item.input, item.response);
      }
      return item.evaluation >= qualityThreshold;
    });
    
    if (goodResponses.length < 3) return; // Not enough good responses yet
    
    // Extract patterns from good responses
    for (const item of goodResponses) {
      const inputConcepts = this._extractKeyConcepts(item.input);
      const responseConcepts = this._extractKeyConcepts(item.response);
      
      // Create a pattern key from the most important concepts
      const patternConcepts = [...new Set([...inputConcepts, ...responseConcepts])].slice(0, 3);
      if (patternConcepts.length < 2) continue; // Need at least 2 concepts for a meaningful pattern
      
      const patternKey = patternConcepts.sort().join('|');
      
      // Check if pattern already exists
      if (!this.insightPatterns.has(patternKey)) {
        // Create new pattern
        this.insightPatterns.set(patternKey, {
          concepts: patternConcepts,
          template: this._extractResponseTemplate(item.response, responseConcepts),
          examples: [item.response],
          created: Date.now(),
          usageCount: 0
        });
      } else {
        // Update existing pattern
        const pattern = this.insightPatterns.get(patternKey);
        if (!pattern.examples.includes(item.response)) {
          pattern.examples.push(item.response);
        }
        this.insightPatterns.set(patternKey, pattern);
      }
    }
  }
  
  // Extract template from a good response
  _extractResponseTemplate(response, concepts) {
    // Create a template by replacing specific concepts with placeholders
    let template = response;
    
    for (const concept of concepts) {
      // Only replace standalone instances of the concept (with word boundaries)
      const conceptRegex = new RegExp(`\\b${concept}\\b`, 'gi');
      template = template.replace(conceptRegex, '{{concept}}');
    }
    
    return template;
  }
  
  // Identify higher-level meta-patterns
  _identifyMetaPatterns() {
    // Need sufficient response patterns first
    if (this.insightPatterns.size < 5) return;
    
    // Find recurring structural elements across patterns
    const templates = Array.from(this.insightPatterns.values())
      .map(pattern => pattern.template);
    
    // Identify question patterns (responses with questions)
    this._extractQuestionMetaPatterns(templates);
    
    // Identify perspective-shift patterns
    this._extractPerspectiveShiftPatterns(templates);
    
    // Identify concept elaboration patterns
    this._extractConceptElaborationPatterns(templates);
    
    // Identify implicit insight patterns
    this._extractImplicitInsightPatterns(templates);
  }
  
  // Extract question patterns
  _extractQuestionMetaPatterns(templates) {
    const questionTemplates = templates.filter(t => t.includes('?'));
    if (questionTemplates.length < 2) return;
    
    // Extract question forms
    const questions = [];
    for (const template of questionTemplates) {
      const parts = template.split('?');
      // Get the question part (last part before question mark)
      for (let i = 0; i < parts.length - 1; i++) {
        const questionText = parts[i].split('.').pop().trim();
        if (questionText.length > 10) {
          questions.push(questionText + '?');
        }
      }
    }
    
    if (questions.length < 2) return;
    
    // Create question meta-pattern if not exists
    const existingPattern = this.metaPatterns.find(p => p.type === 'question-reframe');
    
    if (!existingPattern) {
      this.metaPatterns.push({
        type: 'question-reframe',
        templates: questions,
        keywords: this._extractCommonWords(questions),
        created: Date.now()
      });
      
      this._logSystemEvent(`Identified question meta-pattern with ${questions.length} templates`);
    } else {
      // Update existing pattern with new templates
      const newTemplates = questions.filter(q => !existingPattern.templates.includes(q));
      existingPattern.templates.push(...newTemplates);
      
      // Update keywords
      existingPattern.keywords = this._extractCommonWords(existingPattern.templates);
    }
  }
  
  // Extract perspective shift patterns
  _extractPerspectiveShiftPatterns(templates) {
    const perspectiveMarkers = [
      "from another perspective", "alternatively", "on the other hand",
      "looking at this differently", "another way to see this"
    ];
    
    const perspectiveTemplates = templates.filter(t => 
      perspectiveMarkers.some(marker => t.toLowerCase().includes(marker))
    );
    
    if (perspectiveTemplates.length < 2) return;
    
    // Extract the perspective shift parts
    const perspectives = [];
    for (const template of perspectiveTemplates) {
      for (const marker of perspectiveMarkers) {
        if (template.toLowerCase().includes(marker)) {
          const parts = template.toLowerCase().split(marker);
          if (parts.length > 1) {
            // Get text after the marker until next punctuation
            const perspectiveText = parts[1].split(/[.!?]/).shift().trim();
            if (perspectiveText.length > 10) {
              perspectives.push(perspectiveText);
            }
          }
        }
      }
    }
    
    if (perspectives.length < 2) return;
    
    // Create meta-pattern or update existing
    const existingPattern = this.metaPatterns.find(p => p.type === 'perspective-shift');
    
    if (!existingPattern) {
      this.metaPatterns.push({
        type: 'perspective-shift',
        templates: perspectives,
        keywords: this._extractCommonWords(perspectives),
        created: Date.now()
      });
      
      this._logSystemEvent(`Identified perspective-shift meta-pattern with ${perspectives.length} templates`);
    } else {
      // Update existing pattern
      const newTemplates = perspectives.filter(p => !existingPattern.templates.includes(p));
      existingPattern.templates.push(...newTemplates);
      existingPattern.keywords = this._extractCommonWords(existingPattern.templates);
    }
  }
  
  // Extract concept elaboration patterns
  _extractConceptElaborationPatterns(templates) {
    // Look for concept elaboration patterns where {{concept}} is explained
    const elaborationTemplates = templates.filter(t => 
      t.includes('{{concept}}') && 
      (t.includes('means') || t.includes('refers to') || t.includes('is defined as'))
    );
    
    if (elaborationTemplates.length < 2) return;
    
    // Create meta-pattern or update existing
    const existingPattern = this.metaPatterns.find(p => p.type === 'concept-elaboration');
    
    if (!existingPattern) {
      this.metaPatterns.push({
        type: 'concept-elaboration',
        templates: elaborationTemplates,
        keywords: this._extractCommonWords(elaborationTemplates),
        created: Date.now()
      });
      
      this._logSystemEvent(`Identified concept-elaboration meta-pattern with ${elaborationTemplates.length} templates`);
    } else {
      // Update existing pattern
      const newTemplates = elaborationTemplates.filter(p => !existingPattern.templates.includes(p));
      existingPattern.templates.push(...newTemplates);
      existingPattern.keywords = this._extractCommonWords(existingPattern.templates);
    }
  }
  
  // Extract implicit insight patterns
  _extractImplicitInsightPatterns(templates) {
    const insightMarkers = [
      "interestingly", "surprisingly", "notably", "importantly",
      "significantly", "critically", "fundamentally"
    ];
    
    const insightTemplates = templates.filter(t => 
      insightMarkers.some(marker => t.toLowerCase().includes(marker))
    );
    
    if (insightTemplates.length < 2) return;
    
    // Extract insight statements
    const insights = [];
    for (const template of insightTemplates) {
      for (const marker of insightMarkers) {
        if (template.toLowerCase().includes(marker)) {
          const parts = template.toLowerCase().split(marker);
          if (parts.length > 1) {
            // Get text after the marker until next punctuation
            const insightText = parts[1].split(/[.!?]/).shift().trim();
            if (insightText.length > 10) {
              insights.push(marker + " " + insightText);
            }
          }
        }
      }
    }
    
    if (insights.length < 2) return;
    
    // Create meta-pattern or update existing
    const existingPattern = this.metaPatterns.find(p => p.type === 'implicit-insight');
    
    if (!existingPattern) {
      this.metaPatterns.push({
        type: 'implicit-insight',
        templates: insights,
        keywords: this._extractCommonWords(insights),
        created: Date.now()
      });
      
      this._logSystemEvent(`Identified implicit-insight meta-pattern with ${insights.length} templates`);
    } else {
      // Update existing pattern
      const newTemplates = insights.filter(p => !existingPattern.templates.includes(p));
      existingPattern.templates.push(...newTemplates);
      existingPattern.keywords = this._extractCommonWords(existingPattern.templates);
    }
  }
  
  // Extract common words from a set of texts
  _extractCommonWords(texts) {
    // Flatten all texts into word array
    const allWords = texts.join(' ').toLowerCase()
      .replace(/[^\w\s]/g, ' ')
      .split(/\s+/)
      .filter(w => w.length > 3);
      
    // Filter stop words
    const stopWords = ["this", "that", "these", "those", "there", "their", "they", "have", 
                      "with", "from", "about", "some", "what", "when", "where", "which"];
    
    const filteredWords = allWords.filter(word => !stopWords.includes(word));
    
    // Count frequencies
    const wordCounts = {};
    filteredWords.forEach(word => {
      wordCounts[word] = (wordCounts[word] || 0) + 1;
    });
    
    // Get words that appear in at least 20% of texts
    const threshold = Math.max(2, Math.floor(texts.length * 0.2));
    
    return Object.entries(wordCounts)
      .filter(([_, count]) => count >= threshold)
      .map(([word]) => word);
  }
  
  // Analyze overall system performance
  analyzeSystemPerformance() {
    // Ensure we have enough data
    if (this.responseHistory.length < 5) {
      this._logSystemEvent("Not enough interaction history for performance analysis");
      return false;
    }
    
    // Calculate overall metrics
    const overallQuality = this.responseHistory
      .slice(-10) // Last 10 interactions
      .map(item => {
        if (item.evaluation === null) {
          item.evaluation = this._evaluateResponseQuality(item.input, item.response);
        }
        return item.evaluation;
      })
      .reduce((sum, quality) => sum + quality, 0) / 10;
    
    // Identify improvement opportunities
    const weakestMetric = Object.entries(this.performanceMetrics)
      .sort(([_, a], [__, b]) => a - b)[0][0];
    
    // Generate improvement strategy
    let strategyText = ``;
    switch (weakestMetric) {
      case 'coherence':
        strategyText = `Focusing on improving response coherence by strengthening transitions between ideas and ensuring consistent concept flow.`;
        this.reflectionLevel = Math.min(5, this.reflectionLevel + 1);
        break;
        
      case 'diversity':
        strategyText = `Prioritizing response diversity by incorporating more varied expression patterns and reducing repetition.`;
        break;
        
      case 'relevance':
        strategyText = `Enhancing input relevance by more closely analyzing query concepts and ensuring they're addressed in responses.`;
        break;
        
      case 'depth':
        strategyText = `Increasing conceptual depth by developing more nuanced perspectives on abstract concepts.`;
        this.reflectionLevel = Math.min(5, this.reflectionLevel + 1);
        break;
        
      case 'learning':
        strategyText = `Accelerating pattern learning by more actively identifying and generalizing from successful response structures.`;
        break;
    }
    
    // Log performance analysis
    const analysisText = `
      Performance Analysis:
      Overall quality: ${(overallQuality * 100).toFixed(1)}%
      Strongest area: ${Object.entries(this.performanceMetrics).sort(([_, a], [__, b]) => b - a)[0][0]}
      Improvement focus: ${weakestMetric}
      Strategy: ${strategyText}
    `;
    
    this._logSystemEvent(analysisText);
    
    // Update UI
    const insights = document.getElementById('metaCognitionInsights');
    if (insights) {
      insights.innerHTML = analysisText.split('\n').map(line => 
        `<div class="text-xs mb-1">${line.trim()}</div>`
      ).join('');
    }
    
    // Update reflection level display
    const reflectionLevel = document.getElementById('reflectionLevel');
    if (reflectionLevel) {
      reflectionLevel.textContent = this.reflectionLevel;
    }
    
    return true;
  }
  
  // Log system event to improvement log
  _logSystemEvent(message) {
    const timestamp = new Date().toLocaleTimeString();
    const logEntry = `[${timestamp}] ${message}`;
    
    console.log(`Meta-Cognition: ${logEntry}`);
    this.selfImprovementLog.push(logEntry);
    
    // Keep log size limited
    if (this.selfImprovementLog.length > 100) {
      this.selfImprovementLog.shift();
    }
    
    // Update insights display if visible
    const insights = document.getElementById('metaCognitionInsights');
    if (insights && !insights.classList.contains('hidden')) {
      insights.innerHTML = this.selfImprovementLog.slice(-5).map(entry => 
        `<div class="text-xs mb-1">${entry}</div>`
      ).join('');
    }
  }
}

// Create and initialize the meta-cognition system
window.metaCognitionSystem = new MetaCognitionSystem().initialize();

// Override the original sendInput function to incorporate meta-cognition
const originalSendInput = window.sendInput;

window.sendInput = async function() {
  const input = userInput.value.trim();
  if (!input) return;

  addMessage('You', input);
  userInput.value = '';
  showTyping();

  try {
    // Run original Wikipedia lookups and processing
    const words = input.toLowerCase().split(/\s+/);
    let lookupPromises = words.map(async word => {
      if (word.length > 3 && !['this', 'that', 'with', 'from'].includes(word)) {
        return {
          word,
          data: await wikipediaLearner.fetchWikipediaInfo(word)
        };
      }
      return null;
    });

    // Process Wikipedia lookups
    const lookupResults = await Promise.all(lookupPromises);
    const validLookups = lookupResults.filter(result => result && result.data);

    // Generate response using multiple learning techniques
    let response = "";
    
    // Process Wikipedia content and update context systems
    if (validLookups.length > 0) {
      validLookups.forEach(lookup => {
        if (lookup.data && lookup.data.description) {
          // Process with context mapper
          contextMapper.processWikipediaText(lookup.data.description, lookup.word);
          
          // Add learning insights to response
          const learningInsight = wikipediaLearner.generateLearningInsights(lookup.word, lookup.data);
          response += learningInsight + " ";
          
          // Update advanced engine with the same data
          if (window.advancedEngine) {
            window.advancedEngine.processInput(lookup.data.description, false);
          }
        }
      });
    }

    // Generate response from appropriate engine
    let engineResponse = "";
    let responseSource = "";
    
    if (window.advancedEngine) {
      // Use advanced contextual engine if available
      engineResponse = window.advancedEngine.generateResponse(input);
      responseSource = "advancedEngine";
    } else {
      // Fallback to original context mapper
      engineResponse = contextMapper.generateContextualResponse(input);
      responseSource = "contextMapper";
    }
    
    // Combine responses
    if (response.length > 0) {
      // If we have Wikipedia content, add the engine response
      response += " " + engineResponse;
    } else {
      // Otherwise just use the engine response
      response = engineResponse;
    }
    
    // Apply meta-cognitive enhancement if enabled
    if (window.metaCognitionSystem && window.metaCognitionSystem.enabled) {
      response = window.metaCognitionSystem.processInteraction(input, response, responseSource);
    }

    // Add bot message
    addMessage('Bot', response);

    // Learn from the interaction with original systems
    const tokens = tokenize(input);
    tokens.forEach(([key, value]) => {
      // Update training data
      trainingData.push({ input: key, output: value });
      updatePhraseMap(key, value);
    });

    // Retrain neural network
    net.train(trainingData, { 
      iterations: 100, 
      errorThresh: 0.02 
    });

    // Save memory
    saveMemory();
    
    // Update visualizations
    updateContextVisualizations();

  } catch (error) {
    console.error('Input processing error:', error);
    addMessage('Bot', 'Sorry, I encountered an error processing your input.');
  } finally {
    hideTyping();
    drawGraph();
  }
};

function updateSimilarityInsights(input, response) {
  const similarityInsights = document.getElementById('similarityInsights');
  if (!similarityInsights) return;
  
  // Get similarity with recent responses
  const similarResponses = findSimilarPhrases(input);
  
  if (similarResponses.length === 0) {
    similarityInsights.innerHTML = '<div class="text-gray-500">No similar previous interactions found.</div>';
    return;
  }
  
  // Calculate similarity between current response and similar past responses
  const responseSimilarities = similarResponses.map(item => ({
    phrase: item.phrase,
    output: item.output,
    similarity: calculateSimilarity(response, item.output)
  }));
  
  // Sort by similarity to current response
  responseSimilarities.sort((a, b) => b.similarity - a.similarity);
  
  // Display insights
  const insightHtml = `
    <div class="text-sm font-medium text-indigo-600 mb-1">Response similarity analysis:</div>
    ${responseSimilarities.slice(0, 3).map(item => `
      <div class="mb-2">
        <div class="flex items-center">
          <span class="text-xs font-medium">Input: "${item.phrase}"</span>
          <span class="similarity-badge">${Math.round(item.similarity * 100)}% similar</span>
        </div>
        <div class="text-xs text-gray-600 ml-2">Response: "${item.output.substring(0, 60)}${item.output.length > 60 ? '...' : ''}"</div>
      </div>
    `).join('')}
    
    ${window.metaCognitionSystem && window.metaCognitionSystem.enabled ? 
      `<div class="text-xs text-purple-600 mt-2">
        Meta-cognition has analyzed this pattern and made ${responseSimilarities[0].similarity > 0.7 ? 'significant' : 'minor'} adjustments to the response.
      </div>` : ''}
  `;
  
  similarityInsights.innerHTML = insightHtml;
  
  // If meta-cognition is enabled, record this similarity pattern
  if (window.metaCognitionSystem && window.metaCognitionSystem.enabled) {
    // Find high-similarity responses that might indicate repetitive patterns
    const highSimilarityResponses = responseSimilarities.filter(item => item.similarity > 0.6);
    
    if (highSimilarityResponses.length > 0) {
      window.metaCognitionSystem._logSystemEvent(
        `Detected ${highSimilarityResponses.length} similar previous responses (${Math.round(highSimilarityResponses[0].similarity * 100)}% max similarity)`
      );
    }
  }
}

// Modify the original saveMemory function to also save meta-cognition data
const originalSaveMemory = window.saveMemory;

window.saveMemory = function() {
  // Call the original function
  originalSaveMemory();
  
  // Save meta-cognition data if available
  if (window.metaCognitionSystem) {
    window.metaCognitionSystem._saveMetaCognitionData();
  }
};
</script>
"""
    
    def _inject_into_getdata(self):
        """Helper method to inject code into getmodeldata.php"""
        try:
            with open(self.files['getdata'], 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add meta-cognition data paths
            pathsInjection = """$brainModelPath = $modelsDir . '/brain_model.json';
$metaCognitionPath = $dataDir . '/meta_cognition.json';
$metaPatternPath = $dataDir . '/meta_patterns.json';"""
            
            # Replace original paths declaration
            content = content.replace(
                "$brainModelPath = $modelsDir . '/brain_model.json';", 
                pathsInjection
            )
            
            # Add meta-cognition data to response structure
            responseDataInjection = """'data' => [
        'trainingData' => [],
        'phraseMap' => [],
        'sentenceStructures' => [],
        'contextualMemory' => [],
        'brainModel' => null,
        'metaCognition' => null,
        'metaPatterns' => []"""
            
            # Replace original data structure
            content = content.replace(
                """'data' => [
        'trainingData' => [],
        'phraseMap' => [],
        'sentenceStructures' => [],
        'contextualMemory' => [],
        'brainModel' => null""",
                responseDataInjection
            )
            
            # Add code to load meta-cognition data
            loadMetaDataInjection = """
// Load brain model if exists
if (file_exists($brainModelPath)) {
    $brainModel = json_decode(file_get_contents($brainModelPath), true);
    if ($brainModel !== null) {
        $response['data']['brainModel'] = $brainModel;
        $response['stats']['hasModel'] = true;
    }
}

// Load meta-cognition data if exists
if (file_exists($metaCognitionPath)) {
    $metaCognition = json_decode(file_get_contents($metaCognitionPath), true);
    if ($metaCognition !== null) {
        $response['data']['metaCognition'] = $metaCognition;
        $response['stats']['hasMetaCognition'] = true;
    }
}

// Load meta patterns if exists
if (file_exists($metaPatternPath)) {
    $metaPatterns = json_decode(file_get_contents($metaPatternPath), true);
    if ($metaPatterns !== null) {
        $response['data']['metaPatterns'] = $metaPatterns;
        $response['stats']['metaPatternsCount'] = count($metaPatterns);
    }
}"""
            
            # Replace original model loading code
            content = content.replace(
                """// Load brain model if exists
if (file_exists($brainModelPath)) {
    $brainModel = json_decode(file_get_contents($brainModelPath), true);
    if ($brainModel !== null) {
        $response['data']['brainModel'] = $brainModel;
        $response['stats']['hasModel'] = true;
    }
}""",
                loadMetaDataInjection
            )
            
            # Write the modified content
            with open(self.files['getdata'], 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Successfully injected meta-cognition support into {self.files['getdata']}")
            
        except Exception as e:
            print(f"Error injecting into {self.files['getdata']}: {e}")
    
    def _inject_into_savedata(self):
        """Helper method to inject code into savemodeldata.php"""
        try:
            with open(self.files['savedata'], 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add meta-cognition data paths
            pathsInjection = """$brainModelPath = $modelsDir . '/brain_model.json';
$metaCognitionPath = $dataDir . '/meta_cognition.json';
$metaPatternPath = $dataDir . '/meta_patterns.json';"""
            
            # Replace original paths declaration
            content = content.replace(
                "$brainModelPath = $modelsDir . '/brain_model.json';", 
                pathsInjection
            )
            
            # Add meta-cognition save code
            saveMetaDataInjection = """
// Save brain model if provided
if (isset($data['brainModel']) && !empty($data['brainModel'])) {
    file_put_contents($brainModelPath, json_encode($data['brainModel']));
}

// Save meta-cognition data if provided
if (isset($data['metaCognition']) && !empty($data['metaCognition'])) {
    file_put_contents($metaCognitionPath, json_encode($data['metaCognition'], JSON_PRETTY_PRINT));
    $stats['metaCognitionSaved'] = true;
}

// Save meta patterns if provided
if (isset($data['metaPatterns']) && is_array($data['metaPatterns'])) {
    file_put_contents($metaPatternPath, json_encode($data['metaPatterns'], JSON_PRETTY_PRINT));
    $stats['metaPatternsSaved'] = count($data['metaPatterns']);
}"""
            
            # Replace original model save code
            content = content.replace(
                """// Save brain model if provided
if (isset($data['brainModel']) && !empty($data['brainModel'])) {
    file_put_contents($brainModelPath, json_encode($data['brainModel']));
}""",
                saveMetaDataInjection
            )
            
            # Write the modified content
            with open(self.files['savedata'], 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Successfully injected meta-cognition support into {self.files['savedata']}")
            
        except Exception as e:
            print(f"Error injecting into {self.files['savedata']}: {e}")

# Additional server integration for meta-cognition data
def add_server_sync_code(injector):
    """Add additional server sync code to index.html"""
    try:
        with open(injector.files['index'], 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add server sync code after the existing sync functions
        serverSyncCode = """
// Add integration with server endpoints for meta-cognition data
async function syncServerMetaCognition() {
  if (!window.metaCognitionSystem) return;
  
  try {
    // Prepare meta-cognition data for server
    const metaCognitionData = {
      insightPatterns: Array.from(window.metaCognitionSystem.insightPatterns.entries()),
      metaPatterns: window.metaCognitionSystem.metaPatterns,
      performanceMetrics: window.metaCognitionSystem.performanceMetrics,
      lastSync: Date.now()
    };
    
    // Prepare LSTM model data (already handled by existing sync)
    
    // Construct the data to send
    const dataToSend = {
      metaCognition: metaCognitionData,
      metaPatterns: window.metaCognitionSystem.metaPatterns,
    };
    
    // Only sync if server sync is enabled
    if (typeof SAVE_ENDPOINT !== 'undefined') {
      console.log('Syncing meta-cognition data with server...');
      
      // Send data to server
      const response = await fetch(SAVE_ENDPOINT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend)
      });
      
      const result = await response.json();
      
      if (result.success) {
        console.log('Meta-cognition data synced successfully!', result.stats);
        window.metaCognitionSystem._logSystemEvent('Server sync complete');
      } else {
        console.error('Failed to sync meta-cognition data:', result.message);
      }
    }
  } catch (error) {
    console.error('Error syncing meta-cognition data:', error);
  }
}

// Override the original saveMemory function to also sync meta-cognition data
const superSaveMemory = window.saveMemory;
window.saveMemory = function() {
  // Call the enhanced save function
  superSaveMemory();
  
  // Also sync with server if needed
  syncServerMetaCognition();
};

// Add this script at the end of the existing code
document.addEventListener('DOMContentLoaded', function() {
  // Initialize meta-cognition system if not already initialized
  if (!window.metaCognitionSystem) {
    window.metaCognitionSystem = new MetaCognitionSystem().initialize();
    console.log('Meta-cognition system initialized');
  }
  
  // Add meta-cognition reset button to the control panel
  const controlsDiv = document.querySelector('.flex.gap-4.mt-4');
  if (controlsDiv) {
    const resetMetaButton = document.createElement('button');
    resetMetaButton.className = 'bg-purple-500 text-white px-4 py-2 rounded-xl hover:bg-purple-600 transition';
    resetMetaButton.textContent = 'Reset Meta-Cognition';
    resetMetaButton.onclick = function() {
      if (confirm('Are you sure you want to reset the meta-cognition system? This will clear all learned patterns and insights.')) {
        window.metaCognitionSystem = new MetaCognitionSystem().initialize();
        alert('Meta-cognition system has been reset.');
      }
    };
    
    controlsDiv.appendChild(resetMetaButton);
  }
  
  // Try to load from server
  if (typeof GET_ENDPOINT !== 'undefined') {
    // Load server data and initialize meta-cognition if available
    fetch(GET_ENDPOINT)
      .then(response => response.json())
      .then(result => {
        if (result.success && result.data) {
          // Initialize meta-cognition with server data if available
          if (result.data.metaCognition) {
            console.log('Initializing meta-cognition from server data');
            
            // Parse meta-cognition data
            const metaData = result.data.metaCognition;
            
            // Initialize with server data
            if (window.metaCognitionSystem) {
              window.metaCognitionSystem.insightPatterns = new Map(metaData.insightPatterns || []);
              window.metaCognitionSystem.metaPatterns = metaData.metaPatterns || [];
              window.metaCognitionSystem.performanceMetrics = metaData.performanceMetrics || window.metaCognitionSystem.performanceMetrics;
              
              window.metaCognitionSystem._logSystemEvent(
                `Loaded ${window.metaCognitionSystem.insightPatterns.size} patterns, ${window.metaCognitionSystem.metaPatterns.length} meta-patterns from server`
              );
              
              // Update UI
              window.metaCognitionSystem._updateUIState();
            }
          }
        }
      })
      .catch(error => {
        console.error('Error loading server data:', error);
      });
  }
});"""
        
        # Find the position to insert server sync code - after the existing saveMemory function
        insertPosition = content.find("// Add this function to visualize semantic network")
        if insertPosition == -1:
            # Fallback - add at the end of the script
            insertPosition = content.rfind("</script>")
        
        if insertPosition != -1:
            # Insert the server sync code
            updatedContent = content[:insertPosition] + serverSyncCode + "\n\n" + content[insertPosition:]
            
            # Write the modified content
            with open(injector.files['index'], 'w', encoding='utf-8') as f:
                f.write(updatedContent)
                
            print("Successfully added server sync code for meta-cognition data")
        else:
            print("Could not find suitable position to insert server sync code")
            
    except Exception as e:
        print(f"Error adding server sync code: {e}")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Meta-Cognition Injector for Enhanced Cleverbot'
    )
    
    parser.add_argument('--backup', action='store_true', 
        help='Create backup of original files before modification')
    parser.add_argument('--inject', action='store_true',
        help='Inject meta-cognition code into the system')
    
    args = parser.parse_args()
    
    # Create injector instance
    injector = MetaCognitionInjector(args.backup)
    
    # Execute requested actions
    if args.backup:
        injector.create_backup()
    
    if args.inject:
        injector.inject_meta_cognition()
        # Add additional server sync code
        add_server_sync_code(injector)
        
        print("\nMeta-cognition system has been successfully injected!")
        print("\nThe bot now has the ability to:")
        print("1. Recursively analyze and refine its own responses")
        print("2. Track and avoid repetitive patterns")
        print("3. Build a library of successful response templates")
        print("4. Identify high-level meta-patterns in communication")
        print("5. Continuously evaluate and improve its own performance")
        print("\nYou can control the meta-cognition system using the new UI panel.")