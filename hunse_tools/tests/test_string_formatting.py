from hunse_tools.string_formatting import format_magnitude, format_memory


def test_format_memory():
    sections = dict(
        integers=[0, 9, 10, 100, 1023, 1024, 2e6, 5e10],
        floats=[0.0, 1.1, 9.9, 10.0, 100.3, 1023.99, 1024],
        small=[0.1, 0.001, 0.9, 1e-9],
        negative=[-1, -0.0001, -5, -9.9, -10],
    )
    print()
    for section, values in sections.items():
        print(f"--- {section}")
        for x in values:
            print(f"{x}: {format_memory(x)}")


def test_format_magnitude():
    sections = dict(
        integers=[0, 9, 10, 100, 999, 1000, 2e6, 5e10],
        floats=[0.0, 1.1, 9.9, 10.0, 100.3, 1023.99, 1024],
        small=[0.1, 0.001, 0.9, 1e-9],
        negative=[-1, -0.0001, -5, -9.9, -10, -1001, -2e6],
    )
    print()
    for section, values in sections.items():
        print(f"--- {section}")
        for x in values:
            print(f"{x}: {format_magnitude(x)}")
