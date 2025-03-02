<h1 align="center"><b>Generic ML Project</b></h1>

flowchart TD
    %% Core ML Modules
    subgraph "Core ML Modules"
        DI["Data Ingestion"]:::core
        DT["Data Transformation"]:::core
        MT["Model Trainer"]:::core
    end

    %% Pipeline Orchestration
    subgraph "Pipeline Orchestration"
        TP["Train Pipeline"]:::pipeline
        PP["Predict Pipeline"]:::pipeline
    end

    %% Supporting Services
    subgraph "Supporting Services"
        LOG["Logger"]:::support
        EX["Exception Management"]:::support
        UT["Utility Functions"]:::support
    end

    %% Data Flow Connections
    DI -->|"transfers"| DT
    DT -->|"feedsInto"| MT

    %% Pipeline Integrations
    DI -->|"triggers"| TP
    DT -->|"supplies"| TP
    MT -->|"initiates"| TP
    MT -->|"serves"| PP

    %% Support Services Connections
    LOG ---|"supports"| DI
    LOG ---|"supports"| DT
    LOG ---|"supports"| MT
    LOG ---|"supports"| TP
    LOG ---|"supports"| PP

    EX ---|"monitors"| DI
    EX ---|"monitors"| DT
    EX ---|"monitors"| MT
    EX ---|"monitors"| TP
    EX ---|"monitors"| PP

    UT ---|"assists"| DI
    UT ---|"assists"| DT
    UT ---|"assists"| MT
    UT ---|"assists"| TP
    UT ---|"assists"| PP

    %% Click Events
    click DI "https://github.com/csn1101/generic_ml_project/blob/main/src/components/data_ingestion.py"
    click DT "https://github.com/csn1101/generic_ml_project/blob/main/src/components/data_transformation.py"
    click MT "https://github.com/csn1101/generic_ml_project/blob/main/src/components/model_trainer.py"
    click TP "https://github.com/csn1101/generic_ml_project/blob/main/src/pipeline/train_pipeline.py"
    click PP "https://github.com/csn1101/generic_ml_project/blob/main/src/pipeline/predict_pipeline.py"
    click LOG "https://github.com/csn1101/generic_ml_project/blob/main/src/logger.py"
    click EX "https://github.com/csn1101/generic_ml_project/blob/main/src/exception.py"
    click UT "https://github.com/csn1101/generic_ml_project/blob/main/src/utils.py"

    %% Styles
    classDef core fill:#f9c,stroke:#333,stroke-width:2px;
    classDef pipeline fill:#bbf,stroke:#333,stroke-width:2px;
    classDef support fill:#cfc,stroke:#333,stroke-width:2px;