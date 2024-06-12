# -*- coding: utf-8 -*-
"""ops_tests.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zZvsJS5SC1ezebAeR_qSLBGf7_kc25Ws

[
    {
        "name": "alice",
        "inputs": ["a"],
        "outputs": ["a_add_b", "a_mul_c"]
    },
    {
        "name": "bob",
        "inputs": ["b"],
        "outputs": ["a_add_b", "a_mul_c"]
    }
]
"""

in1txt = "in1";
in2txt = "in2";
outtxt = "out";
ops = ["add", "div", "eq", "gt", "geq", "lt", "leq", "mul", "neq", "sub"];

N = 100;

list = [ { "name": "alice", "inputs": [], "outputs": [] }, { "name": "bob", "inputs": [], "outputs": [] } ]
in1dict = {};
in2dict = {};
for i in range(N):
  for op in ops:
    in1ops = in1txt + "_" + op + "["+ str(i) + "]";
    in2ops = in2txt + "_" + op + "["+ str(i) + "]";
    outops = outtxt + "_" + op + "["+ str(i) + "]";
    list[0]['inputs'].append(in1ops);
    list[0]['outputs'].append(outops);
    list[1]['inputs'].append(in2ops);
    list[1]['outputs'].append(outops);
    in1dict[in1ops] = 1;
    in2dict[in2ops] = 1;

print(list);
print(in1dict);
print(in2dict);

import json
with open('mpc_settings.json', 'w') as fp:
    json.dump(list, fp)

with open('inputs_party_0.json', 'w') as fp:
    json.dump(in1dict, fp)

with open('inputs_party_1.json', 'w') as fp:
    json.dump(in2dict, fp)

aops = {"add": "+", "div": "/", "eq": "==", "gt": ">", "geq": ">=", "lt": "<", "leq": "<=", "mul": "*", "neq": "!=", "sub": "-"};
aops

lines = [];

for aopk in aops:
  # print("out = in0" + aopv + "in1");
  lines.append("for i in range(" + str(N) + "):\n");
  lines.append("\t")
  lines.append("in1 = sint.get_input_from(1);\n");
  lines.append("\t")
  lines.append("in0 = sint.get_input_from(0);\n");
  lines.append("\t")
  lines.append("out = in0" + aops[aopk] + "in1;\n");
  lines.append("\t")
  lines.append("print_ln_to(1, 'out=%s', out.reveal_to(1));\n")
  lines.append("\t")
  lines.append("print_ln_to(0, 'out=%s', out.reveal_to(0));\n")

print(lines)

with open('raw_circuit.mpc', 'w') as fp:
    for line in lines:
      fp.write(line);