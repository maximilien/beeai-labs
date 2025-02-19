#! /bin/bash
echo "validate 🗒️ agents.yaml"
maestro validate ../../../schemas/agent_schema.json ./agents.yaml

echo "validate 🗒️ workflow.yaml"
maestro validate ../../../schemas/workflow_schema.json  ./workflow.yaml

echo "run 🏃🏽‍♂️‍➡️ workflow.yaml"
../maestro run ./agents.yaml ./workflow.yaml