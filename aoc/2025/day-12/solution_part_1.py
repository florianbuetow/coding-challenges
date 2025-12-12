# O(m * k^k) time and O(n + k) space where n=shapes, m=regions, k=max region area
# link: https://adventofcode.com/2025/day/12

class Solution:
	def computeNumberOfRegionsThatFitAllPresents(self, filename) -> int:

		def getShapesAndRegions():
			shapes = {}
			regions = []
			with open(filename, "r") as fh:
				shapeLinesToParse = 0
				for line in fh:
					line = line.strip()
					if not line: continue
					if 'x' in line:
						dimensions, presents = line.split(': ')
						width, height = [int(part) for part in dimensions.split('x')]
						presents = [int(count) for count in presents.split()]
						regions.append([width, height, presents])
					elif ':' in line:
						shape_id = int(line[:line.find(':')])
						shapes[shape_id] = []
						shapeLinesToParse = float('inf')
					elif shapeLinesToParse > 0:
						if shapeLinesToParse == float('inf'):
							shapeLinesToParse = len(line)
						shapes[shape_id].append(line)
						shapeLinesToParse -= 1
			return shapes, regions

		def getCanvas(width, height):
			return [['?'] * width for _ in range(height)]

		def getAllOrientations(shape):
			orientations = set()
			shape = tuple(shape)
			for _ in range(4):
				shape = tuple(''.join(s) for s in zip(*shape[::-1]))
				orientations.add(shape)
				flipped = tuple(row[::-1] for row in shape)
				orientations.add(flipped)
			return list(orientations)

		def getShapeArea(shape):
			return sum(row.count('#') for row in shape)

		def canPlaceShapeOnCanvas(canvas, shape, x, y):
			shape_height, shape_width = len(shape), len(shape[0])
			canvas_height, canvas_width = len(canvas), len(canvas[0])
			if x + shape_width > canvas_width: return False
			if y + shape_height > canvas_height: return False
			for sy in range(shape_height):
				for sx in range(shape_width):
					if shape[sy][sx] == '#' and canvas[y + sy][x + sx] != '?':
						return False
			return True

		def placeShapeOnCanvas(canvas, shape, x, y):
			for sy in range(len(shape)):
				for sx in range(len(shape[0])):
					if shape[sy][sx] == '#':
						canvas[y + sy][x + sx] = '#'

		def removeShapeFromCanvas(canvas, shape, x, y):
			for sy in range(len(shape)):
				for sx in range(len(shape[0])):
					if shape[sy][sx] == '#':
						canvas[y + sy][x + sx] = '?'

		def canPlaceAllShapes(canvas, shape_ids, idx, orientations, start_y, start_x):
			if idx == len(shape_ids):
				return True
			canvas_height, canvas_width = len(canvas), len(canvas[0])
			shape_id = shape_ids[idx]
			for y in range(start_y, canvas_height):
				x_begin = start_x if y == start_y else 0
				for x in range(x_begin, canvas_width):
					for shape in orientations[shape_id]:
						if canPlaceShapeOnCanvas(canvas, shape, x, y):
							placeShapeOnCanvas(canvas, shape, x, y)
							if canPlaceAllShapes(canvas, shape_ids, idx + 1, orientations, y, x):
								return True
							removeShapeFromCanvas(canvas, shape, x, y)
			return False

		shapes, regions = getShapesAndRegions()
		orientations = {sid: getAllOrientations(shape) for sid, shape in shapes.items()}
		areas = {sid: getShapeArea(shape) for sid, shape in shapes.items()}

		result = 0
		for region in regions:
			canvas_width, canvas_height, presents = region

			shape_ids = []
			for shape_id, count in enumerate(presents):
				shape_ids.extend([shape_id] * count)
			shape_ids.sort(key=lambda sid: areas[sid], reverse=True)

			required_area = sum(areas[sid] for sid in shape_ids)
			if required_area > canvas_width * canvas_height:
				continue

			canvas = getCanvas(canvas_width, canvas_height)
			if canPlaceAllShapes(canvas, shape_ids, 0, orientations, 0, 0):
				result += 1

		return result

if __name__ == '__main__':
	s = Solution()
	print(s.computeNumberOfRegionsThatFitAllPresents('input_0.txt'))
	print(s.computeNumberOfRegionsThatFitAllPresents('input_1.txt'))
