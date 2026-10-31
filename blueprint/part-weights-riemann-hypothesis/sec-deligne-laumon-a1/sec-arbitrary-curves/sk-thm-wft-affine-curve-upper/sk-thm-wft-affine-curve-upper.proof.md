+++
kind = "proof"
of = "sk-thm-wft-affine-curve-upper"
+++
We push the sheaf
forward to the line and realize $H^1_c$ as a quotient of a group
bounded by Theorem [sk-thm-dl-a1-upper]. Choose $\pi$ as in
Lemma [sk-lem-wft-finite-map] and put $K=\pi_*j_!F$. Let $W_0$ be the dense
open on which $K$ is lisse and pure. Since its complement is finite,
localization gives

$$
H_c^1(W,K|_W)\twoheadrightarrow
H_c^1(\mathbf A^1,K)=H_c^1(C,F).
$$

By Lemma [sk-lem-wft-infinity-reduction], after a finite extension of
the constant field there is a further surjection from $H_c^1(V,G)$
onto $H_c^1(W,K|_W)$, with $G$ pure of weight $w$ and unramified at
infinity. Let $v:V\hookrightarrow\mathbf A^1$ be the inclusion and
$i:Z\hookrightarrow\mathbf A^1$ its finite complement. The
localization sequence for $v_*G$ reads

$$
H_c^0(Z,i^*v_*G)\longrightarrow H_c^1(V,G)
\longrightarrow H_c^1(\mathbf A^1,v_*G)\longrightarrow0.
$$

The first group has weights at most $w$ by
Proposition [sk-p-real-semi], and the last has weights at most $w+1$ by
Theorem [sk-thm-dl-a1-upper]. Hence the middle group has weights
at most $w+1$. The bound passes to quotients under the two
surjections, and by Lemma [sk-lem-wft-infinity-reduction] it holds over
the original constant field.
