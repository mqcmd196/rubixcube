from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from getch import getch, pause
import sys

distance = 5.0
pitch = 0.0
yaw = 0.0

mouse_button = -1
mouse_x = 0
mouse_y = 0

light_position = [1.0, 1.0, 1.0, 0.0]
light_ambient = [0.4, 0.4, 0.4, 1.0]
light_diffuse = [1.0, 1.0, 1.0, 1.0]

mat_default_color = [1.0, 1.0, 1.0, 1.0]
mat_default_specular = [1.0, 1.0, 1.0, 1.0]
mat_default_shininess = [100.0]
mat_default_emission = [0.0, 0.0, 0.0, 0.0]

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glShadeModel(GL_SMOOTH)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_default_color)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_default_color)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_default_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_default_shininess)

def display():
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, distance, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotatef(-pitch, 1.0, 0.0, 0.0 )
    glRotatef(-yaw, 0.0, 1.0, 0.0 )
    glPushMatrix()
    # glutSolidTeapot(1.5)
    # ここにルービックキューブを表示させたいわね
    glutSolidCube(2.0)

    glPopMatrix()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w)/float(h), 0.1, 20.0)

def keyboard(key, x, y):
    key = ord(getch())
    print(key)
    sys.exit()

def mouse(button, state, x, y):
    global mouse_button
    global mouse_x
    global mouse_y

    mouse_button = button
    mouse_x = x
    mouse_y = y

    if state == GLUT_UP:
        mouse_button = -1
    
    glutPostRedisplay()

def motion(x, y):
    global mouse_x
    global mouse_y
    global distance
    global mouse_button
    global yaw
    global pitch

    if mouse_button == GLUT_LEFT_BUTTON:
        if(x == mouse_x and y == mouse_y):
            return 
        yaw += -(x - mouse_x) / 10.0
        pitch += -(y - mouse_y) / 10.0

    elif mouse_button == GLUT_RIGHT_BUTTON:
        if(y == mouse_y):
            return
        elif(y < mouse_y):
            distance += (mouse_y - y) / 50.0
        else:
            distance -= (y - mouse_y) / 50.0

        if distance < 1.0:
            distance = 1.0
        elif distance > 10.0:
            distance = 10.0

    mouse_x = x
    mouse_y = y

    glutPostRedisplay()

def idle():
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)     # window size
    glutInitWindowPosition(50, 50) # window position
    glutCreateWindow("teapot")      # show window
    init()
    glutDisplayFunc(display)         # draw callback function
    glutReshapeFunc(reshape)         # resize callback function
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()

if __name__ == "__main__":
    main()
