stages = [
    # 0 wrong guesses: Empty Gallows
    """
       +---+

       |   |
           |

           |
           |
           |
    =========
    """,
    # 1 wrong guess: Head
    """
       +---+

       |   |
       O   |

           |
           |
           |
    =========
    """,
    # 2 wrong guesses: Torso
    """
       +---+

       |   |
       O   |

       |   |
           |

           |
    =========
    """,
    # 3 wrong guesses: Left Arm
    """
       +---+
       |   |
       O   |
      /|   |

           |
           |
    =========
    """,
    # 4 wrong guesses: Right Arm
    r"""
       +---+

       |   |
       O   |
      /|\  |

           |
           |
    =========
    """,
    # 5 wrong guesses: Left Leg
    r"""
       +---+

       |   |
       O   |
      /|\  |
      /    |

           |
    =========
    """,
    # 6 wrong guesses: Right Leg (Game Over)
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]
