# Python AST (syntax tree) examples for lunch-n-learn

Slides: https://docs.google.com/presentation/d/1Ri40Kb5aE9uz-DcHvuWwx-o_0mRtIIY4WoPHY0nLIcc/edit?usp=sharing

To run the completed code:

    cd done

    # Create a virtualenv in a directory called env.
    python3 -m venv env

    # Activate that virtualenv. Note the space after the dot.
    . env/bin/activate

    # --isolated may be needed if you run this on a Crunchbase computer, but can
    # be omitted otherwise. (--isolated runs pip with the default settings, ignoring
    # CB's package index, which may be configured on your computer. If using the CB
    # package index, pip will fail to find astor)
    pip3 install --isolated astor

    # Run the example code files. Look at their source code to see what's going on.
    python3 solution.py
    python3 hello-world.py
