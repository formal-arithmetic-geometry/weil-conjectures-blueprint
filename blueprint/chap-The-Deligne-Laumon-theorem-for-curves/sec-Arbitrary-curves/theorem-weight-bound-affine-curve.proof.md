+++
kind = "proof"
of = "theorem-weight-bound-affine-curve"
order = 1316
uses = ["lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "proposition-six-operations-dctf", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-weights-under-usual-operations", "lemma-degree-zero-top-cohomology", "definition-middle-extension", "proposition-weights-j-boundary-points", "lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "theorem-weight-bound-affine-line", "lemma-finite-quasi-finite-direct-images"]
+++
We push the sheaf forward to the line and realize $H^1_c$ as a
quotient of a group bounded by
Theorem [theorem-weight-bound-affine-line]. This uses two
surjections: one removes the points where the direct image fails
to be lisse and pure, and the other moves a lisse point to infinity.

Choose $\pi$ as in
Lemma [lemma-finite-generically-etale-map-line] and put $K=\pi_*j_!F$. Let $W_0$ be the dense
open on which $K$ is lisse and pure. Since its complement is finite,
localization gives

$$
H_c^1(W,K|_W)\twoheadrightarrow
H_c^1(\mathbf A^1,K)=H_c^1(C,F).
$$

By Lemma [lemma-finite-extension-base-field-moving], after a finite extension of
the constant field there is a further surjection from $H_c^1(V,G)$
onto $H_c^1(W,K|_W)$, with $G$ pure of weight $w$ and unramified at
infinity. Let $v:V\hookrightarrow\mathbf A^1$ be the inclusion and
$i:Z\hookrightarrow\mathbf A^1$ its finite complement. The
localization sequence for $v_*G$ reads

$$
H_c^0(Z,i^*v_*G)\longrightarrow H_c^1(V,G)
\longrightarrow H_c^1(\mathbf A^1,v_*G)\longrightarrow0.
$$

The first group has weights at most $w$. Indeed, the stalks of
$i^*v_*G$ at the closed points of $Z_0$ have weights at most $w$ by
Proposition [proposition-weights-j-boundary-points], and
$H_c^0(Z,i^*v_*G)$ is the direct sum, over the closed points $z$ of $Z_0$,
of the stalks at the $e=[\kappa(z):k_m]$ geometric points over $z$, where
$k_m$ is the constant field of $V_0$. The geometric Frobenius of $k_m$
permutes these $e$ stalks cyclically, and its $e$th power on each of them
is conjugate to the local Frobenius $F_z$. An eigenvalue $\beta$ on such a
cycle therefore satisfies $\beta^e=\alpha$ for an eigenvalue $\alpha$ of
$F_z$, so that $|\iota\beta|^e=|\iota\alpha|\le q_z^{w/2}=(q^m)^{ew/2}$,
and $|\iota\beta|\le(q^m)^{w/2}$, which is weight at most $w$ over $k_m$.
This is the case of the finite map $Z_0\to\operatorname{Spec}k_m$ in
Lemma [lemma-finite-quasi-finite-direct-images], whose proof is the same
computation. The last group has weights at most $w+1$ by
Theorem [theorem-weight-bound-affine-line]. As an extension of a
subgroup of the last by a quotient of the first, the middle group therefore has
weights at most $w+1$. This bound passes to quotients under the two
surjections, and by Lemma [lemma-weight-bound-constant-extension] it holds over
the original constant field.
