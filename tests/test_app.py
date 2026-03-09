from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_project.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse tem teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa o SUT
    - A: Assert  - Garanta que A é A
    """

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK
