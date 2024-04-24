from click.testing import CliRunner
import run 

def test_call_hello():
    runner = CliRunner()
    result=  runner.invoke(run.hello)
    assert result.exit_code == 0
    assert "Hello" in result.output
    
def test_call_add():
    runner = CliRunner()
    result=  runner.invoke(run.add ['carrots'])
    assert result.exit_code == 0
    assert "CARROTS added!" in result.output

def test_call_remove():
    runner = CliRunner()
    result=  runner.invoke(run.remove ['carrots'])
    assert result.exit_code == 0
    assert "CARROTS removed!" in result.output
