+++
kind = "proof"
of = "lem-weil-pbc-henselian-of-nil-maximal-ideal"
+++
For a polynomial f and x with f(x) in the maximal ideal and f'(x) a unit, f(x) is nilpotent. Mathlib's Polynomial.existsUnique_nilpotent_sub_and_aeval_eq_zero supplies a with f(a)=0 and x-a nilpotent. Its finite Newton-iteration proof squares the error at each step; nilpotent corrections preserve invertibility of the derivative. If f(x)^N=0, an iteration with 2^n >= N has zero error. The negative a-x of the nilpotent difference lies in every prime ideal (nilradical_le_prime), hence in the maximal ideal. This is precisely HenselianLocalRing.is_henselian.
