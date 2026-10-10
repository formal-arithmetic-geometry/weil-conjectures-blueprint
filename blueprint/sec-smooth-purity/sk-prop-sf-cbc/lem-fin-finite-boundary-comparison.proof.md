+++
kind  = "proof"
of    = "lem-fin-finite-boundary-comparison"
+++
Let $M$ be the cone of $c$.
Its restriction to $G$ is zero. The termwise localization
sequence for extension by zero in
[def-weil-pbc-extension-by-zero], verified on stalks by
[lemma-weil-pbc-geometric-stalk-conservative], identifies
$M=i_*i^*M$.
Therefore

$$
0=Rb_*M=R(bi)_*i^*M=(bi)_*i^*M,
$$

the last equality using finite exactness in
[lemma-weil-pbc-finite-direct-image-exact].
Finite direct image is conservative: its stalks are the products
in [lemma-weil-pbc-finite-stalk-formula], so a zero direct image
forces every stalk on its source to be zero.
Apply this to every cohomology sheaf of $i^*M$.
It follows that $i^*M=0$, hence $M=0$ and $c$ is an isomorphism.
