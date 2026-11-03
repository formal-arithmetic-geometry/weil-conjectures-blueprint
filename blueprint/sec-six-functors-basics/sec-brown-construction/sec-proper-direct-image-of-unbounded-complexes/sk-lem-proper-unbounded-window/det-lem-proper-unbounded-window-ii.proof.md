+++
kind = "proof"
of    = "det-lem-proper-unbounded-window-ii"
+++
First let $(M_\alpha)$ be a family with cohomology in a common finite interval of degrees. Then the map
$\bigoplus_\alpha Rp_*M_\alpha\to Rp_*(\bigoplus_\alpha M_\alpha)$ is an isomorphism in
$\D(Y_{\mathrm{proét}},\Lambda)$, by induction on the length of the interval. For length zero, $M_\alpha$ is a
shifted object of $\IndCons(X,\Lambda)$, and this is the direct-sum assertion of
[sk-lem-proper-heart-bound] in each degree. For the inductive step, sum the truncation triangles that split
off the top cohomology sheaf and apply the five lemma to the long exact cohomology sequences
([det-proper-unbounded-window-ii-bounded]).

Now let $(K_\alpha)$ be arbitrary and fix $q$. Direct sums of sheaves are exact, so cohomology and
truncations commute with direct sums. The objects $\tau_{\geq q-2d-1}\tau_{\leq q}K_\alpha$ have cohomology in
the common interval $[q-2d-1,q]$. Applying the window isomorphism [det-proper-unbounded-window-iso] to
each $K_\alpha$ and to $\bigoplus_\alpha K_\alpha$, and the first paragraph to the truncated family, shows
that $\bigoplus_\alpha Rp_*K_\alpha\to Rp_*(\bigoplus_\alpha K_\alpha)$ is an isomorphism on $\mathcal H^q$. As
$q$ is arbitrary, it is an isomorphism ([det-proper-unbounded-window-ii-general]).
