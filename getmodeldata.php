<?php
/**
 * getmodeldata.php - Simple endpoint for retrieving Cleverbot training data
 */

// Set headers to allow cross-origin requests
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

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

// Paths for different types of data
$trainingDataPath = $dataDir . '/training_data.json';
$phraseMapPath = $dataDir . '/phrase_map.json';
$sentenceStructuresPath = $dataDir . '/sentence_structures.json';
$contextualMemoryPath = $dataDir . '/contextual_memory.json';
$brainModelPath = $modelsDir . '/brain_model.json';
$metaCognitionPath = $dataDir . '/meta_cognition.json';
$metaPatternPath = $dataDir . '/meta_patterns.json';

// Initialize response data
$response = [
    'success' => true,
    'data' => [
        'trainingData' => [],
        'phraseMap' => [],
        'sentenceStructures' => [],
        'contextualMemory' => [],
        'brainModel' => null,
        'metaCognition' => null,
        'metaPatterns' => []
    ],
    'stats' => [
        'trainingDataCount' => 0,
        'phraseMapCount' => 0,
        'sentenceStructuresCount' => 0,
        'contextualMemoryCount' => 0,
        'hasModel' => false
    ]
];

// Load training data if exists
if (file_exists($trainingDataPath)) {
    $trainingData = json_decode(file_get_contents($trainingDataPath), true);
    if ($trainingData !== null) {
        $response['data']['trainingData'] = $trainingData;
        $response['stats']['trainingDataCount'] = count($trainingData);
    }
}

// Load phrase map if exists
if (file_exists($phraseMapPath)) {
    $phraseMap = json_decode(file_get_contents($phraseMapPath), true);
    if ($phraseMap !== null) {
        // Convert associative array to array format expected by client
        $phraseMapArray = [];
        foreach ($phraseMap as $key => $values) {
            $phraseMapArray[] = [$key, $values];
        }
        $response['data']['phraseMap'] = $phraseMapArray;
        $response['stats']['phraseMapCount'] = count($phraseMapArray);
    }
}

// Load sentence structures if exists
if (file_exists($sentenceStructuresPath)) {
    $sentenceStructures = json_decode(file_get_contents($sentenceStructuresPath), true);
    if ($sentenceStructures !== null) {
        $response['data']['sentenceStructures'] = $sentenceStructures;
        $response['stats']['sentenceStructuresCount'] = count($sentenceStructures);
    }
}

// Load contextual memory if exists
if (file_exists($contextualMemoryPath)) {
    $contextualMemory = json_decode(file_get_contents($contextualMemoryPath), true);
    if ($contextualMemory !== null) {
        // Convert associative array to array format expected by client
        $contextualMemoryArray = [];
        foreach ($contextualMemory as $key => $values) {
            $contextualMemoryArray[] = [$key, $values];
        }
        $response['data']['contextualMemory'] = $contextualMemoryArray;
        $response['stats']['contextualMemoryCount'] = count($contextualMemoryArray);
    }
}


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
}

// Return the data
echo json_encode($response);
