+++
kind  = "proof"
of    = "thm-weil-pbc-henselian-idempotent-lifting"
uses = ["thm-weil-pbc-stein-inputs"]
+++
Not proved in this blueprint; it is the object-level half of the classical
proper base change package for henselian pairs. The argument: by input (ii)
of [thm-weil-pbc-stein-inputs], every connected component of $Z$ meets $Z_0$.
So every open and closed subscheme of $Z_0$ is the closed fibre of one of
$Z$, which gives surjectivity on idempotents. Uniqueness holds because
distinct open and closed subschemes of $Z$ have distinct traces on $Z_0$.

The restriction map $H^0(Z,\mathcal O_Z)\to H^0(Z_0,\mathcal O_{Z_0})$ itself
is not an isomorphism. For $A=k[[t]]$, $I=(t)$ and $Z=\mathbf P^1_A$ it is
$k[[t]]\to k$. So only idempotents are compared. The locally constant form of
the Zariski restriction criterion does not apply to $\mathcal O_Z$, which is
not a torsion sheaf, so this correspondence has to be supplied separately.
