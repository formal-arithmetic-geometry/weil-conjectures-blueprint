+++
kind = "proof"
of = "sk-thm-dl-a1-upper"
uses = ["sk-r-real-linear"]
+++
We first prove the bound for the irreducible
factors of $F$ and then pass to $F$ by induction. Take a finite
composition series of the finite-dimensional Weil representation of
$F$. Each irreducible lisse factor is pure of weight $w$, since its
local eigenvalues are eigenvalues of a subquotient, and it is again
unramified at infinity, since inertia at infinity acts trivially on
every subquotient of a representation on which it acts trivially. An irreducible factor that is geometrically
constant is a sheaf $\mathcal B_b$ of Proposition [sk-r-real-linear],
because the geometric action is
trivial and an invertible linear operator over $\overline{\mathbf Q}_\ell$ has an
eigenline. Its middle extension is constant on the affine line, and
its $H_c^1$ vanishes by the trivial case of
Lemma [sk-lem-wft-character-integral]. By the last assertion of
Proposition [sk-p-dl-a1-middle], no other factor $F_i$ has a
geometric constituent of the form $\mathcal L_{\psi(ax)}$, and hence
Corollary [sk-c-dl-a1-hc1], applied with $M=F_i$, applies to it.

By Proposition [sk-p-dl-a1-exact], the short exact sequences of
the composition series remain exact after applying $j_*$. Consider a
step $0\to F'\to F''\to F_i\to0$ of the series. In the resulting long
exact sequence of compactly supported cohomology, the image of
$H^1_c(\mathbf A^1,j_*F')$ in $H^1_c(\mathbf A^1,j_*F'')$ is a
quotient of the former, and the cokernel embeds in
$H^1_c(\mathbf A^1,j_*F_i)$. Since the bound $w+1$
is preserved under subquotients and extensions, we conclude by
induction that it holds for $F$.
