+++
kind = "proof"
of = "proposition-proper-base-change-projective-line--2"
order = 380004
uses = ["proposition-proper-base-change-projective-line--1", "theorem-pbc-injective-acyclicity"]
+++
Apply [proposition-proper-base-change-projective-line--1] to $I$ placed
in degree zero. Since $I$ is injective, $R\pi_*I$ is concentrated in
degree zero; exactness of $g^*$ gives the same assertion for
$g^*R\pi_*I$. Base change identifies this complex with
$R\pi'_*g'^*I$, whose positive cohomology sheaves therefore vanish.
This is the forward implication from the base change property to
injective acyclicity in [theorem-pbc-injective-acyclicity]; this
implication needs no torsion hypothesis on the coefficient ring.
