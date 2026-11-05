+++
kind = "proof"
of = "lemma-finite-extension-base-field-moving"
order = 1310
+++
We delete a rational point where $F$ is lisse, which replaces $H^1_c$
by a group surjecting onto it, and move that point to infinity by an
automorphism of $\mathbf P^1$. First choose a closed point of $W_0$ and a finite
extension $k_m$ of the constant field over which it has a rational
point $s$.
The restriction of $F$ to $W_0\otimes_{k_0}k_m$ is again pure of
weight $w$, because a residue extension raises an eigenvalue and the
residue cardinality to the same power.
Next, some element of $\mathrm{PGL}_2(k_m)$ sends $s$ to infinity, and we
transport $F|_{W\setminus\{s\}}$ by this automorphism. As $F$ is
lisse at $s$, its local inertia there is trivial, so the
transported sheaf $G$ extends to a lisse sheaf across the new infinity.
It is defined on the image $V_0$ of
$W_0\setminus\{s\}$, a dense open of the affine line, and
$H^1_c(V,G)=H^1_c(W\setminus\{s\},F)$ because the automorphism
identifies the two pairs. The surjection follows from the localization
sequence

$$
H_c^1(W\setminus\{s\},F)\to H_c^1(W,F)\to H_c^1(\{s\},F_{\bar s})=0,
$$

in which the last group vanishes because a point has no cohomology in
positive degrees. Since every construction is defined over $k_m$, the
map commutes with the Frobenius of $k_m$.
