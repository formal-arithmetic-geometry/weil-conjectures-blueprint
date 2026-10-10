+++
kind  = "proof"
of    = "sk-thm-trace-formula"
+++
First prove the formula for every closed subscheme of the affine
line, uniformly over all finite extensions. For a finite scheme,
[sk-i-topology] permits reduction, preserving the Weil maps,
compact cohomology, and geometric stalks. Being reduced of dimension
zero, its geometric base change is a finite disjoint union of spectra of
finite extensions, hence of points (06LH).
Frobenius permutes their perfect stalk complexes; the chain
supertrace in [sk-p-trace] receives contributions only from
the diagonal blocks, exactly the fixed points.

For $\mathbf A^1$, extend the [sk-d-weil] datum by zero to
the projective line of [sk-d-lines], which is proper (0FMG)
and smooth of pure dimension one (0B2P).
Open base change and composition in [sk-thm-sf-package] identify its
compact cohomology and global operator with the originals.
Apply [sk-c-proper-global] on this smooth proper curve, then
[sk-p-local] and [sk-p-frob]. The coefficient stalk at
$\infty$ is zero, so its computed local term is zero.
Finally a closed subscheme of $\mathbf A^1_F$ has coordinate ring
$F[t]/I$. If $I=0$, it is the line; otherwise a nonzero polynomial
in $I$ makes the quotient finite-dimensional over $F$, and the
finite-scheme case applies. This includes nonreduced schemes.

Now prove the formula for all affine schemes with a presentation
$F[t_1,\ldots,t_n]/I$, by induction on $n$, simultaneously over all
finite extensions and for every Weil complex and every iterate.
The cases $n\le1$ were just proved. For $n\ge2$, forget $t_n$ to
obtain $f_0:X_0\to Y_0=\mathbf A^{n-1}_F$. Use the Weil
$!$-pushforward $(L,\psi)$ of [sk-d-weil-push].
Its compact global operator is conjugate to the original one.
Induction on $Y_0$ gives

$$
\tr_A(F_{c,m},R\Gamma_c(X,K))
=\sum_{y\in Y_0(\mathbf F_{q^m})}\tr_A(\psi_{m,\bar y},L_{\bar y}).
$$

Base change identifies the operator at $\bar y$ with the compact
Frobenius operator on the fiber, considered over $\mathbf F_{q^m}$
with one-step Weil map $\varphi_m$. This follows by pasting the
base-change squares and relative-Frobenius units defining $\psi_m$.
The fiber is a closed subscheme of the affine line over that field,
so the base case computes its trace. Summing over the fibers gives
the rational-point sum on $X_0$.

For a general separated finite-type scheme, take a finite affine
cover $U_1,\ldots,U_N$ and the affine pieces
$U_i\setminus\bigcup_{j<i}U_j$. The successive closed complements
give a finite localization filtration. Repeated
[sk-i-global-additivity] combines their proven trace formulas;
their rational points form the same disjoint partition.
