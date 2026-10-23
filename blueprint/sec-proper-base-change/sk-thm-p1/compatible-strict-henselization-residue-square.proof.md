+++
kind = "proof"
of = "compatible-strict-henselization-residue-square"
+++
The maps $\rho_A$ and $\rho_B$ correspond to field embeddings $\kappa_A\to k$ and $\kappa_B\to k'$. The image of
the composite $\kappa_A\to k\to k'$ lies in the image of $\kappa_B$, so there is a unique embedding
$r:\kappa_A\to\kappa_B$ whose composite with $\kappa_B\to k'$ is $\kappa_A\to k\to k'$; its ring laws follow from
injectivity of $\kappa_B\to k'$, and $\operatorname{Spec}(r)\circ\rho_B=\rho_A\circ\iota$ follows since
$\operatorname{Spec}$ is fully faithful. Lift $r$ through the universal property of strict henselization (Stacks
Project, Tags 04GU and 04HX) to a ring map $\varphi:A\to B$ compatible with the structure maps, which gives the
first equality. The ring residue diagram commutes and field embeddings and residue projections are local, so
$\varphi$ is local. Surjectivity of $B\to\kappa_B$ identifies $r$ with the residue map $\bar\varphi$.
