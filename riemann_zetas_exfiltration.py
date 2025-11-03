import argparse
import logging
import sympy as sp
from sympy import zeta, N, re, im
import cmath

# Logging: For the Father speaks of truths and errors
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class ZetaExfiltrator:
    def __init__(self, precision=30):
        sp.mpmath.mp.dps = precision  # Set decimal precision for computations

    def compute_zeta(self, s_str):
        """Compute zeta(s) for a complex s."""
        try:
            s = complex(s_str)
            s_sym = sp.sympify(s)
            result = N(zeta(s_sym))
            logger.info(f"ζ({s}) ≈ {result}")
            return result
        except ValueError:
            logger.error(f"Invalid complex number: {s_str}")
            return None

    def approximate_zero(self, imag_part):
        """Approximate a zero on the critical line: s = 0.5 + t j."""
        s = 0.5 + imag_part * 1j
        return self.compute_zeta(str(s))

    def find_zeros_in_range(self, start, end, steps):
        """Scan for approximate zeros in imag range [start, end] with steps."""
        zeros = []
        dt = (end - start) / steps
        prev_val = self.approximate_zero(start)
        for i in range(1, steps + 1):
            t = start + i * dt
            curr_val = self.approximate_zero(t)
            # Simple sign change detection for real part crossing zero (heuristic)
            if re(prev_val) * re(curr_val) < 0 or abs(curr_val) < 1e-5:
                zeros.append(0.5 + t * 1j)
            prev_val = curr_val
        return zeros

    def batch_compute(self, input_file, output_file):
        """Process batch of s values from input file."""
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                s_str = line.strip()
                if s_str:
                    result = self.compute_zeta(s_str)
                    f_out.write(f"ζ({s_str}) ≈ {result}\n")

    def report_zeros(self, zeros):
        if zeros:
            logger.info("\nApproximated Zeros Exfiltrated:")
            for z in zeros:
                print(z)
        else:
            logger.info("No zeros detected in range. Deepen the scan.")

def main():
    parser = argparse.ArgumentParser(description="RiemannZetasExfiltrator: Exfiltrate zeta values and zeros.")
    subparsers = parser.add_subparsers(dest='command')

    compute_parser = subparsers.add_parser('compute', help='Compute zeta at a point')
    compute_parser.add_argument('--s', type=str, required=True, help='Complex s (e.g., "2+0j")')

    zeros_parser = subparsers.add_parser('zeros', help='Approximate zeros in imag range')
    zeros_parser.add_argument('--start', type=float, default=0, help='Start of imag part')
    zeros_parser.add_argument('--end', type=float, default=100, help='End of imag part')
    zeros_parser.add_argument('--steps', type=int, default=1000, help='Number of steps')

    batch_parser = subparsers.add_parser('batch', help='Batch compute from file')
    batch_parser.add_argument('--input', type=str, required=True, help='Input file with s values')
    batch_parser.add_argument('--output', type=str, required=True, help='Output file for results')

    args = parser.parse_args()

    exfiltrator = ZetaExfiltrator()

    if args.command == 'compute':
        exfiltrator.compute_zeta(args.s)
    elif args.command == 'zeros':
        zeros = exfiltrator.find_zeros_in_range(args.start, args.end, args.steps)
        exfiltrator.report_zeros(zeros)
    elif args.command == 'batch':
        exfiltrator.batch_compute(args.input, args.output)
    else:
        parser.error("Choose a command: compute, zeros, or batch.")

if __name__ == "__main__":
    main()