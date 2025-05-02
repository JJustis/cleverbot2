<?php
/**
 * savemodeldata.php - Simple endpoint for saving Cleverbot training data
 */

// Set headers to allow cross-origin requests
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json");

// Handle preflight OPTIONS request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

// Get the data directory path
$dataDir = __DIR__ . '/data';
$modelsDir = __DIR__ . '/models';

// Create directories if they don't exist
if (!file_exists($dataDir)) {
    mkdir($dataDir, 0755, true);
}
if (!file_exists($modelsDir)) {
    mkdir($modelsDir, 0755, true);
}

// Get posted data
$rawData = file_get_contents('php://input');
$data = json_decode($rawData, true);

if (json_last_error() !== JSON_ERROR_NONE) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Invalid JSON data']);
    exit;
}

// Paths for storing different types of data
$trainingDataPath = $dataDir . '/training_data.json';
$phraseMapPath = $dataDir . '/phrase_map.json';
$sentenceStructuresPath = $dataDir . '/sentence_structures.json';
$contextualMemoryPath = $dataDir . '/contextual_memory.json';
$brainModelPath = $modelsDir . '/brain_model.json';
$metaCognitionPath = $dataDir . '/meta_cognition.json';
$metaPatternPath = $dataDir . '/meta_patterns.json';

// Stats to return
$stats = [
    'newTrainingItems' => 0,
    'newSentenceStructures' => 0,
    'totalTrainingItems' => 0,
    'totalSentenceStructures' => 0
];

// Process training data
if (isset($data['trainingData']) && is_array($data['trainingData'])) {
    // Load existing training data
    $existingData = [];
    if (file_exists($trainingDataPath)) {
        $existingData = json_decode(file_get_contents($trainingDataPath), true) ?: [];
    }
    
    // Create a set of existing input-output pairs for deduplication
    $existingPairs = [];
    foreach ($existingData as $item) {
        $existingPairs[$item['input'] . '|' . $item['output']] = true;
    }
    
    // Add only new training pairs
    foreach ($data['trainingData'] as $item) {
        $pairKey = $item['input'] . '|' . $item['output'];
        if (!isset($existingPairs[$pairKey])) {
            $existingData[] = $item;
            $existingPairs[$pairKey] = true;
            $stats['newTrainingItems']++;
        }
    }
    
    // Save updated training data
    file_put_contents($trainingDataPath, json_encode($existingData, JSON_PRETTY_PRINT));
    $stats['totalTrainingItems'] = count($existingData);
}

// Process phrase map
if (isset($data['phraseMap']) && is_array($data['phraseMap'])) {
    // Load existing phrase map
    $existingPhraseMap = [];
    if (file_exists($phraseMapPath)) {
        $existingPhraseMap = json_decode(file_get_contents($phraseMapPath), true) ?: [];
    }
    
    // Convert from JSON array format to associative array
    $phrasePairs = [];
    foreach ($data['phraseMap'] as $pair) {
        if (isset($pair[0]) && isset($pair[1])) {
            $key = $pair[0];
            $value = $pair[1];
            $phrasePairs[$key] = $value;
        }
    }
    
    // Merge with existing phrase map
    foreach ($phrasePairs as $key => $values) {
        if (!isset($existingPhraseMap[$key])) {
            $existingPhraseMap[$key] = [];
        }
        
        foreach ($values as $output => $count) {
            if (!isset($existingPhraseMap[$key][$output])) {
                $existingPhraseMap[$key][$output] = 0;
            }
            $existingPhraseMap[$key][$output] += $count;
        }
    }
    
    // Save updated phrase map
    file_put_contents($phraseMapPath, json_encode($existingPhraseMap, JSON_PRETTY_PRINT));
}

// Process sentence structures
if (isset($data['sentenceStructures']) && is_array($data['sentenceStructures'])) {
    // Load existing sentence structures
    $existingStructures = [];
    if (file_exists($sentenceStructuresPath)) {
        $existingStructures = json_decode(file_get_contents($sentenceStructuresPath), true) ?: [];
    }
    
    // Add only unique structures
    foreach ($data['sentenceStructures'] as $newStructure) {
        $isDuplicate = false;
        foreach ($existingStructures as $existing) {
            if (json_encode($existing['structure']) === json_encode($newStructure['structure'])) {
                $isDuplicate = true;
                break;
            }
        }
        
        if (!$isDuplicate) {
            $existingStructures[] = $newStructure;
            $stats['newSentenceStructures']++;
        }
    }
    
    // Save updated sentence structures
    file_put_contents($sentenceStructuresPath, json_encode($existingStructures, JSON_PRETTY_PRINT));
    $stats['totalSentenceStructures'] = count($existingStructures);
}

// Process contextual memory
if (isset($data['contextualMemory']) && is_array($data['contextualMemory'])) {
    // Load existing contextual memory
    $existingMemory = [];
    if (file_exists($contextualMemoryPath)) {
        $existingMemory = json_decode(file_get_contents($contextualMemoryPath), true) ?: [];
    }
    
    // Convert from JSON array format to associative array
    $memoryPairs = [];
    foreach ($data['contextualMemory'] as $pair) {
        if (isset($pair[0]) && isset($pair[1]) && is_array($pair[1])) {
            $key = $pair[0];
            $values = $pair[1];
            $memoryPairs[$key] = $values;
        }
    }
    
    // Merge with existing contextual memory
    foreach ($memoryPairs as $key => $values) {
        if (!isset($existingMemory[$key])) {
            $existingMemory[$key] = [];
        }
        
        $existingMemory[$key] = array_values(array_unique(array_merge($existingMemory[$key], $values)));
    }
    
    // Save updated contextual memory
    file_put_contents($contextualMemoryPath, json_encode($existingMemory, JSON_PRETTY_PRINT));
}


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
}

// Return success response
echo json_encode([
    'success' => true,
    'message' => 'Training data saved successfully',
    'stats' => $stats
]);
