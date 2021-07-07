#######################################################################################
#
# 	STANDARD IMPORTS
#

import math

from qiskit import IBMQ, QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit import register

#######################################################################################
#
# 	LOCAL IMPORTS
#


#######################################################################################
#
# 	GLOBAL VARIABLES
#


#######################################################################################
#
# 	HELPER FUNCTIONS
#


#######################################################################################
#
# 	CLASS DEFINITIONS
#


class Adder(object):
    """"""

    def __init__(self):
        pass

    def _create_initialize_input_circuit(self, input: str, register):
        num_bits = register.size
        assert len(input) <= num_bits
        quantum_circuit = QuantumCircuit(register)
        for i in range(len(input)):
            if input[i] == "1":
                quantum_circuit.x(register[num_bits - (i + 1)])
        return quantum_circuit

    def _create_qft_circuit(self, register):
        num_bits = register.size
        quantum_circuit = QuantumCircuit(register)
        quantum_circuit.h(register[num_bits - 1])
        for i in range(0, num_bits - 1):
            quantum_circuit.cu1(
                math.pi / float(2 ** (i + 1)),
                register[num_bits - 1 - (i + 1)],
                register[num_bits - 1],
            )
        return quantum_circuit

    def _create_add_circuit(self, a_register, b_register):
        assert a_register.size == b_register.size
        num_bits = a_register.size
        quantum_circuit = QuantumCircuit(a_register, b_register)
        for i in range(0, num_bits):
            quantum_circuit.cu1(
                math.pi / float(2 ** (i)),
                a_register[num_bits - 1 - i],
                b_register[num_bits - 1],
            )
        return quantum_circuit

    def _create_inverse_qft_circuit(self, register):
        num_bits = register.size
        quantum_circuit = QuantumCircuit(register)
        for i in range(0, num_bits - 1):
            quantum_circuit.cu1(
                -1 * math.pi / float(2 ** (num_bits - 1 - i)),
                register[i],
                register[num_bits - 1],
            )
        quantum_circuit.h(register[num_bits - 1])
        return quantum_circuit

    def create_adder_circuit(self, a: str, b: str):
        # calculate number of bits
        # note that add one bit for carry bit
        num_a_bits = len(a)
        num_b_bits = len(b)
        num_bits = max(num_a_bits, num_b_bits) + 1

        # quantum register for a and b
        a_register = QuantumRegister(num_bits, "a")
        b_register = QuantumRegister(num_bits, "b")

        # qauntum circuit
        quantum_circuit = QuantumCircuit(a_register, b_register)

    def draw_initialize_input_circuit(self, input: str, output: str):
        num_bits = len(input)
        register = QuantumRegister(num_bits)
        return self._create_initialize_input_circuit(input, register).draw(
            output=output
        )

    def draw_qft_circuit(self, num_bits: int, output: str):
        register = QuantumRegister(num_bits)
        return self._create_qft_circuit(register).draw(output=output)

    def draw_add_circuit(self, num_bits: int, output: str):
        a_register = QuantumRegister(num_bits, "a")
        b_register = QuantumRegister(num_bits, "b")
        return self._create_add_circuit(a_register, b_register).draw(output)

    def draw_inverse_qft_circuit(self, num_bits: int, output: str):
        register = QuantumRegister(num_bits)
        return self._create_inverse_qft_circuit(register).draw(output)
