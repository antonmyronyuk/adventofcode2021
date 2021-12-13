VERTEX_NAME_TO_ID_MAP = {}
LOWERCASE_VERTICES = set()
UPPERCASE_VERTICES = set()

with open('input.txt') as input_file:
    lines = [line for line in input_file.read().split('\n') if line]

vertices = set()
for line in lines:
    vertices.update(line.split('-'))

for vertex_id, vertex_name in enumerate(vertices):
    VERTEX_NAME_TO_ID_MAP[vertex_name] = vertex_id

    if vertex_name in ('start', 'end'):
        pass
    elif vertex_name.lower() == vertex_name:
        LOWERCASE_VERTICES.add(vertex_id)
    else:
        UPPERCASE_VERTICES.add(vertex_id)

VERTICES_COUNT = len(vertices)
ADJ_LIST = [[] for _ in range(VERTICES_COUNT)]
for line in lines:
    from_name, to_name = line.split('-')
    from_id = VERTEX_NAME_TO_ID_MAP[from_name]
    to_id = VERTEX_NAME_TO_ID_MAP[to_name]
    ADJ_LIST[from_id].append(to_id)
    ADJ_LIST[to_id].append(from_id)


class PathCounterPart1:
    def __init__(self):
        self.count = 0
        self.visited = [0] * VERTICES_COUNT

    def get_path_count(self):
        self.walk(VERTEX_NAME_TO_ID_MAP['start'], VERTEX_NAME_TO_ID_MAP['end'])
        return self.count

    def walk(self, from_id, to_id):
        if from_id == to_id:
            self.count += 1
            return

        self.visited[from_id] += 1
        for next_id in ADJ_LIST[from_id]:
            if next_id in UPPERCASE_VERTICES or self.visited[next_id] < 1:
                self.walk(next_id, to_id)

        self.visited[from_id] -= 1


class PathCounterPart2:
    def __init__(self):
        self.count = 0
        self.visited = [0] * VERTICES_COUNT
        self.was_lowercase_vertex_visited_twice = False

    def get_path_count(self):
        self.walk(VERTEX_NAME_TO_ID_MAP['start'], VERTEX_NAME_TO_ID_MAP['end'])
        return self.count

    def walk(self, from_id, to_id):
        if from_id == to_id:
            self.count += 1
            return

        self.visited[from_id] += 1
        for next_id in ADJ_LIST[from_id]:
            if next_id in UPPERCASE_VERTICES or self.visited[next_id] < 1:
                self.walk(next_id, to_id)
            elif (
                next_id in LOWERCASE_VERTICES
                and self.visited[next_id] == 1
                and not self.was_lowercase_vertex_visited_twice
            ):
                self.was_lowercase_vertex_visited_twice = True
                self.walk(next_id, to_id)
                self.was_lowercase_vertex_visited_twice = False

        self.visited[from_id] -= 1


if __name__ == '__main__':
    print(PathCounterPart1().get_path_count())
    print(PathCounterPart2().get_path_count())
