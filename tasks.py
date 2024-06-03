from invoke import task
@task
def ls(c):
    c.run('cd ..')
    c.run('ls')
