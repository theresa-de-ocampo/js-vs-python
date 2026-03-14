export const cheatsheetSections = {
  inputOutput: {
    title: 'Input & Output',
    rows: [
      {
        description: 'Logging',
        javascript: [['console.log()']],
        python: [['print()']],
      },
      {
        description: 'User Input',
        javascript: [
          ['// Method 1', 'process.argv.slice(2)'],
          ['// Method 2', '// Built-in readline module'],
          ['// Method 3', '// readline-sync package'],
          ['// Method 4 (browser)', 'prompt()'],
        ],
        python: [['input()']],
      },
      {
        description: 'String Interpolation',
        javascript: [['`Hi ${name}`']],
        python: [['f"Hi {name}"']],
      },
    ],
  },
  comments: {
    title: 'Comments',
    rows: [
      {
        description: 'Single Line Comment',
        javascript: [['// This is a comment']],
        python: [['# This is a comment']],
      },
      {
        description: 'Multi Line Comment',
        javascript: [['/*', 'This is a multiline', 'comment', '*/']],
        python: [
          [
            "'''",
            'Python does not have a dedicated syntax',
            'for multiline comments.',
            'The use of triple quotes is discouraged',
            'as it is actually a string literal.',
            'If it appears on top of a module, class, or function,',
            'Python treats it as a docstring.',
            'So using triple quotes can accidentally',
            'modify documentation.',
            "'''",
          ],
        ],
      },
    ],
  },
  stringManipulation: {
    title: 'String Manipulation',
    rows: [
      {
        description: 'Capitalize first letter',
        javascript: [['str.charAt(0).toUpperCase() + str.slice(1)']],
        python: [['capitalize()']],
      },
      {
        description: 'Title Case',
        javascript: [['// No direct equivalent']],
        python: [['title()']],
      },
      {
        description: 'Uppercase',
        javascript: [['toUpperCase()']],
        python: [['upper()']],
      },
      {
        description: 'Lowercase',
        javascript: [['toLowerCase()']],
        python: [['lower()']],
      },
      {
        description: 'Length of String',
        javascript: [['msg.length']],
        python: [['len(msg)']],
      },
      {
        description: 'Check Substring',
        javascript: [["msg.includes('Python')", "!msg.includes('Python')"]],
        python: [["'Python' in msg", "'Python' not in msg"]],
      },
      {
        description: 'Count Substring Occurrence',
        javascript: [['// No direct equivalent', '// Use Regex']],
        python: [["msg.count('Python')"]],
      },
      {
        description: 'Slice String',
        javascript: [['msg.slice(2)']],
        python: [['msg[2:]']],
      },
      {
        description: 'Find Substring Index',
        javascript: [
          [
            '// No direct equivalent',
            '// Closer concept: findIndex() but it takes in a callback',
          ],
        ],
        python: [["msg.find('H')"]],
      },
      {
        description: 'Replace Substring',
        javascript: [
          [
            '// Strings are immutable',
            "sentence.replace('JavaScript', 'Python')",
          ],
        ],
        python: [
          [
            '// Strings are immutable',
            "sentence.replace('JavaScript', 'Python')",
          ],
        ],
      },
      {
        description: 'Split Strings',
        javascript: [
          [
            "msg.split(' ') // Splits by a single space",
            'msg.split() // Returns original array',
          ],
        ],
        python: [
          [
            "msg.split(' ') // Splits by a single space",
            'msg.split() // Splits by spaces',
          ],
        ],
      },
    ],
  },
  arrays: {
    title: 'Arrays',
    rows: [
      {
        description: 'Collection Type',
        javascript: [['// Arrays can contain mixed types']],
        python: [['# Lists can contain mixed types']],
      },
      {
        description: 'Length',
        javascript: [['fruits.length']],
        python: [['len(fruits)']],
      },
      {
        description: 'Last Element',
        javascript: [['fruits.at(-1)']],
        python: [['fruits[-1]']],
      },
      {
        description: 'Count Occurrences',
        javascript: [
          [
            'fruits.reduce((tally, fruit) => {',
            { text: "return tally + (fruit === 'Orange')", className: 'indent-1' },
            '}, 0)',
          ],
        ],
        python: [["fruits.count('Orange')"]],
      },
      {
        description: 'Slice',
        javascript: [['fruits.slice(2,4)']],
        python: [['fruits[2:4]']],
      },
      {
        description: 'Find Index',
        javascript: [["fruits.findIndex(f => f === 'Orange')"]],
        python: [["fruits.index('Orange')"]],
      },
      {
        description: 'Sort',
        javascript: [['fruits.sort()']],
        python: [['fruits.sort()']],
      },
      {
        description: 'Reverse Sort',
        javascript: [['fruits.sort().reverse()']],
        python: [['fruits.sort(reverse=True)']],
      },
      {
        description: 'Reverse Order',
        javascript: [['fruits.reverse()']],
        python: [['fruits.reverse()']],
      },
      {
        description: 'Sorting Numbers',
        javascript: [
          ['// JS sorts numbers as strings by default', 'tally.sort((a, b) => b - a)'],
        ],
        python: [['# Works normally for numbers', 'tally.sort()']],
      },
      {
        description: 'Minimum Value',
        javascript: [
          [
            'tally.reduce((a, b) => Math.min(a, b))',
            '// Alternative but slower for large arrays',
            'Math.min(...tally)',
          ],
        ],
        python: [['min(tally)']],
      },
      {
        description: 'Maximum Value',
        javascript: [['tally.reduce((total, n) => total + n, 0)']],
        python: [['max(tally)']],
      },
      {
        description: 'Combine Two Arrays',
        javascript: [['const fruitsAndVeggies = fruits.concat(veggies)']],
        python: [['fruits_and_veggies = fruits + veggies']],
      },
      {
        description: 'Extend Existing Array',
        javascript: [['fruits.push(...veggies)']],
        python: [['fruits.extend(veggies)']],
      },
      {
        description: 'Add Element to End',
        javascript: [["fruits.push('Mango')"]],
        python: [["fruits.append('Mango')"]],
      },
      {
        description: 'Insert at Specific Index',
        javascript: [["fruits.splice(index, 0, 'Mango')"]],
        python: [["fruits.insert(index, 'Mango')"]],
      },
      {
        description: 'Remove First Occurrence',
        javascript: [["const i = fruits.indexOf('Orange')", 'if (i !== -1) fruits.splice(i, 1)']],
        python: [["fruits.remove('Orange')"]],
      },
      {
        description: 'Remove Last Element',
        javascript: [['fruits.pop()']],
        python: [['fruits.pop()']],
      },
      {
        description: 'Remove at Specific Index',
        javascript: [['fruits.splice(2, 1)', 'fruits.splice(-2, 1)']],
        python: [['fruits.pop(2)', 'fruits.pop(-2)', 'del fruits[2]']],
      },
      {
        description: 'Empty an Array',
        javascript: [['fruits = []']],
        python: [['fruits = []', 'fruits.clear()', 'fruits = list()']],
      },
      {
        description: 'Shallow Copy',
        javascript: [
          [
            'const newFruits = [...fruits]',
            'const newFruits = fruits.slice()',
            'const newFruits = Array.from(fruits)',
          ],
        ],
        python: [['new_fruits = fruits[:]', 'new_fruits = fruits.copy()', 'new_fruits = list(fruits)']],
      },
      {
        description: 'Deep Copy',
        javascript: [['const newEmployees = structuredClone(employees)']],
        python: [['import copy', 'new_employees = copy.deepcopy(employees)']],
      },
      {
        description: 'Join to String',
        javascript: [["fruits.join(',')"]],
        python: [["','.join(fruits)"]],
      },
    ],
  },
  tuples: {
    title: 'Tuples',
    intro: 'An ordered, fixed-sized collection of elements.',
    rows: [
      {
        description: 'Declaration',
        javascript: [
          [
            '// No direct equivalent, closest:',
            "const fruits = Object.freeze('Orange', 'Apple')",
          ],
          [
            '// Note that the TS Tuple has a different meaning',
            '// It enforces specific types per index, and it is mutable.',
            'let fruits : [name: string, count: int]',
          ],
        ],
        python: [['// Faster access because of immutability', "fruits = ('Orange', 'Apple')"]],
      },
      {
        description: 'Empty a Tuple',
        javascript: [['// No direct equivalent']],
        python: [['fruits = ()', 'fruits = tuple()']],
      },
    ],
  },
  sets: {
    title: 'Sets',
    intro: 'A collection of unique values.',
    rows: [
      {
        description: 'Declaration',
        javascript: [["const myFriends = new Set(['Ros', 'Fe', 'Ros'])"]],
        python: [["my_friends = {'Ros', 'Fe', 'Ros'}"]],
      },
      {
        description: 'Intersection',
        javascript: [['myFriends.intersection(yourFriends)']],
        python: [['my_friends.intersection(your_friends)', 'my_friends & your_friends']],
      },
      {
        description: 'Difference',
        javascript: [['myFriends.difference(yourFriends)']],
        python: [['my_friends.difference(your_friends)', 'my_friends - your_friends']],
      },
      {
        description: 'Union',
        javascript: [['myFriends.union(yourFriends)']],
        python: [['my_friends.union(your_friends)', 'my_friends | your_friends']],
      },
      {
        description: 'Symmetric Difference',
        javascript: [['myFriends.symmetricDifference(yourFriends)']],
        python: [['my_friends.symmetric_difference(your_friends)', 'my_friends ^ your_friends']],
      },
      {
        description: 'Empty a Set',
        javascript: [['myFriends.clear()', 'myFriends = new Set([])']],
        python: [['my_friends = set()']],
      },
    ],
  },
  arithmetic: {
    title: 'Arithmetic',
    rows: [
      {
        description: 'Floor Division',
        javascript: [['Math.floor()']],
        python: [['//']],
      },
      {
        description: 'Round',
        javascript: [['Math.round()']],
        python: [['round()']],
      },
      {
        description: 'Power',
        javascript: [['Math.pow()', '**']],
        python: [['**']],
      },
      {
        description: 'Number Formatting',
        javascript: [['price.toFixed(2)']],
        python: [['f"{price:.2f}"']],
      },
    ],
  },
  typesAndTypeChecking: {
    title: 'Types & Type Checking',
    rows: [
      {
        description: 'No Value',
        javascript: [['null']],
        python: [['None']],
      },
      {
        description: 'Get Variable Type',
        javascript: [['typeof value']],
        python: [['type(value)']],
      },
    ],
  },
  functions: {
    title: 'Functions',
    rows: [
      {
        description: 'Default Parameter Behavior',
        javascript: [
          ['function greeting(name, age=18) { /* body */ }'],
          [
            "greeting('Teriz') // Default Used",
            "greeting('Teriz', undefined) // Default Used",
            "greeting('Teriz', null) // Default NOT Used",
          ],
        ],
        python: [
          [
            'def greeting(name, age=18):',
            { text: '# body', className: 'indent-1' },
          ],
          ["greeting('Teriz') # Default used", "greeting('Teriz', None) # Default NOT used"],
        ],
      },
      {
        description: 'Named Function Arguments',
        javascript: [
          [
            '// JS does not support named arguments',
            '// but you can do:',
            "greeting({ name: 'Teriz', age: 26})",
          ],
        ],
        python: [["greeting(name='Teriz', age=26)"]],
      },
      {
        description: 'Return a Tuple',
        javascript: [['// No direct equivalent']],
        python: [['return amount, tax, total amount']],
      },
      {
        description: 'Return a Set',
        javascript: [['// No direct equivalent']],
        python: [['return { amount, tax, total amount }']],
      },
      {
        description: 'Return an Object',
        javascript: [['return { amount, tax, total amount }']],
        python: [['// TODO: After refresher on dictionaries']],
      },
    ],
  },
}
