+++
kind = "proof"
of = "lem-weil-pbc-henselization-completion-data"
+++
Identify $I^nB=(IB)^n$ by products of ideal generators. For $n=0$ both quotients are zero rings. Turn each bijective quotient map into a ring isomorphism $e_n$. The transition squares commute: both routes send the class of $a$ to the class of $f(a)$.

By the inverse-limit definition `AdicCompletion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)), send a compatible sequence $(x_n)$ to $(e_n(x_n))$. Inverse transition compatibility follows by applying the injective $e_m$ to the desired equality. Hence $(y_n)\mapsto(e_n^{-1}(y_n))$ is the inverse. Coordinate evaluation gives the claimed identity and, on completion images of elements $a$, the equality of composite ring maps. In Lean these maps are constructed by AdicCompletion.liftRingHom and their inverse laws checked by AdicCompletion.ext_evalₐ.
