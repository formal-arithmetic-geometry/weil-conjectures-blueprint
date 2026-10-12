+++
kind  = "proof"
of    = "lem-sc-global-functions"
+++
A global function $f\in H^0(C,\mathcal O_C)\setminus k$ would, by
[lem-sc-morphism-from-function], define a morphism
$C\to\mathbf A^1_k$ whose image is proper (the image of a proper
scheme in a separated finite-type target is proper) and affine, hence
finite by [lem-sc-proper-affine-finite]; but $C$ is connected,
so the image is a single point, a $k$-point (the closed points of a
finite-type $k$-scheme are $k$-valued for $k$ algebraically
closed), say with value $c\in k$. Then $f-c$ vanishes at every
point of $C$, so it is locally nilpotent, hence zero because $C$ is
reduced: $f=c\in k$, a contradiction. (Reducedness is needed:
[def-sc-curves] does not ask for it, and
$\mathbf P^1_k\times_k\operatorname{Spec}k[\varepsilon]/(\varepsilon^2)$
is a proper connected curve with global functions
$k[\varepsilon]/(\varepsilon^2)$.)
