Multi-Agent Content Generation System

Kasparro – Applied AI Engineer Challenge

1. Problem Statement

    The objective of this assignment is to design and implement a modular, agentic automation system that takes a structured product dataset as input and automatically generates multiple types of machine-readable content pages.

    The system must:

    operate strictly on the given input data

    avoid external knowledge or research

    generate content through a multi-agent architecture

    output clean, structured JSON pages

    The focus of this challenge is system design, agent orchestration, modularity, and automation, not content writing or UI development.

2. Solution Overview

    To solve the problem, a multi-agent content generation pipeline was designed using Python.
    Each agent has a single, well-defined responsibility and communicates only through structured data.

    The system processes the product data through the following stages:

    Parsing and validation of raw product data

    Automated generation of categorized user questions

    Reusable content logic transformation

    Template-driven page assembly

    Final JSON output generation

    The architecture is extensible, deterministic, and reusable, allowing new products, templates, or agents to be added with minimal changes.

3. Scope & Assumptions
    Scope

    The system operates only on the provided product dataset.

    Content generation is deterministic and rule-based.

    Output pages are strictly machine-readable JSON.

    The system generates:

    FAQ Page

    Product Description Page

    Comparison Page

    Assumptions

    No external APIs or knowledge sources are allowed.

    The fictional comparison product is internally defined and structured.

    The system is designed for automation and scalability rather than UI rendering.

4. System Design (Core Architecture)
    4.1 High-Level Architecture

    The system follows a pipeline-based orchestration model, where an orchestrator controls the execution flow of independent agents.


            Raw Product Data
                  ↓
            Product Parser Agent
                  ↓
            Question Generator Agent
                  ↓
            Content Logic Blocks
                  ↓ 
            Template Engine
                  ↓
            Page Assembly Agent
                  ↓
            JSON Outputs


    4.2 Agent Design & Responsibilities
        1. Product Parser Agent

            Responsibility: Parse and validate raw product data.

            Input: Raw product dictionary

            Output: Structured Product object

            Purpose: Establish a clean internal data model used by all downstream agents.

        2. Question Generator Agent

            Responsibility: Automatically generate categorized user questions.

            Categories: Informational, Usage, Safety, Skin Type, Purchase

            Input: Parsed product object

            Output: Dictionary of categorized questions

            Purpose: Provide structured inputs for FAQ and content reasoning.

        3. Page Assembly Agent

            Responsibility: Orchestrate templates and logic blocks to assemble final pages.

            Input: Product object and generated questions

            Output: JSON files written to disk

            Purpose: Centralized orchestration without embedding business logic.

    4.3 Content Logic Blocks

            Content logic blocks are pure, reusable transformation units.
        They apply rules to structured data and return structured content.

        Examples:

        Benefits Block

        Usage Block

        Safety Block

        Comparison Block

        These blocks:

        contain no template knowledge

        contain no orchestration logic

        can be reused across multiple page types

    4.4 Template Engine

        Templates define the structure and composition of each page type.

        Each template:

        specifies required fields

        calls relevant content logic blocks

        produces JSON-ready dictionaries

        Implemented templates:

        FAQ Template

        Product Page Template

        Comparison Page Template

        Templates do not perform data generation — they only assemble structured content.

    4.5 Orchestration Model

        The orchestration follows a controller-driven pipeline:

        Agents do not directly invoke each other.

        The main orchestrator (main.py) executes agents in sequence.

        Data flows forward with no hidden state.

        This ensures:

        clarity

        testability

        extensibility

        production-style automation

5. Output Structure

    The system produces three machine-readable JSON files:

    faq.json

    product_page.json

    comparison_page.json

    Each output:

    follows a clean schema

    maps directly from data → logic → template

    is suitable for downstream systems or APIs

6. Design Principles Followed

    Single Responsibility Principle

    Loose Coupling

    High Cohesion

    Deterministic Outputs

    Reusable Components

    Clear Data Contracts

7. Conclusion

    This project demonstrates a production-style agentic automation system that emphasizes modularity, clean design, and structured data flow.

    The system satisfies all assignment requirements by:

    implementing a true multi-agent architecture

    avoiding monolithic or prompt-based designs

    producing clean, structured JSON outputs

    maintaining strict separation between data, logic, and orchestration