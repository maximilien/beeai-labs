# SPDX-License-Identifier: Apache-2.0
from enum import StrEnum
from typing import Callable, Type, Union

from .frameworks.beeai_agent import BeeAIAgent, BeeAILocalAgent
from .frameworks.crewai_agent import CrewAIAgent
from .frameworks.openai_agent import OpenAIAgent
from .frameworks.remote_agent import RemoteAgent
from .frameworks.mock_agent import MockAgent

EMOJIS = {
    'beeai': '🐝',
    'crewai': '👥',
    'openai': '🔓',
    'mock': '🤖',
    'remote': '💸',

    # # Not yet supported
    # 'langflow': '⛓',
}

class AgentFramework(StrEnum):
    """Enumeration of supported frameworks"""
    BEEAI = "beeai"
    CREWAI = "crewai"
    OPENAI = 'openai'
    MOCK = 'mock'
    REMOTE = 'remote'

    # Not yet supported
    # LANGFLOW = 'langflow'

class AgentFactory:
    """Factory class for handling agent frameworks"""
    @staticmethod
    def create_agent(framework: AgentFramework, mode="local") -> Callable[..., Union[BeeAIAgent, BeeAILocalAgent, CrewAIAgent, OpenAIAgent, RemoteAgent, MockAgent]]:
        """Create an instance of the specified agent framework.

        Args:
            framework (AgentFramework): The framework to create. Must be a valid enum value.

        Returns:
            A new instance of the corresponding agent class.
        """
        factories = {
            AgentFramework.BEEAI: BeeAILocalAgent,
            AgentFramework.CREWAI: CrewAIAgent,
            AgentFramework.OPENAI: OpenAIAgent,
            AgentFramework.MOCK: MockAgent
        }

        remote_factories = {
            AgentFramework.BEEAI: BeeAIAgent,
            AgentFramework.REMOTE: RemoteAgent,
            AgentFramework.MOCK: MockAgent
        }

        if framework not in factories and framework not in remote_factories:
            raise ValueError(f"Unknown framework: {framework}")

        if mode == "remote" or framework == AgentFramework.REMOTE:
            return remote_factories[framework]
        else:
            return factories[framework]
        
        return factories[framework]

    @classmethod
    def get_factory(cls, framework: str, mode="local") -> Callable[..., Union[BeeAIAgent, BeeAILocalAgent, CrewAIAgent, OpenAIAgent, RemoteAgent, MockAgent]]:
        """Get a factory function for the specified agent type."""
        return cls.create_agent(framework, mode)
