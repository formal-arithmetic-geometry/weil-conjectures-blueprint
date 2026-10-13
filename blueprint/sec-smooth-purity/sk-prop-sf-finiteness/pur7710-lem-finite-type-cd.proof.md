+++
kind = "proof"
of = "pur7710-lem-finite-type-cd"
+++
If $W$ is empty, every sheaf on $W_{\Et}$ is zero and the bound holds. Otherwise let $\epsilon:W_{\Et}\to W_{\mathrm{Zar}}$ be the change of topology and $F$ a torsion abelian sheaf on $W_{\Et}$. The stalk of $R^q\epsilon_*F$ at $w\in W$ is the filtered colimit of $H^q(V_{\Et},F|_V)$ over affine open neighbourhoods $V$ of $w$; these have dimension at most $d$, and $F|_V$ is torsion, so the stalks vanish for $q>d+c$ by Input [pur7710-input-affine-cd]. The Noetherian topological space $W$ has dimension at most $d$, so its Zariski cohomology vanishes above degree $d$ by Grothendieck's vanishing theorem (Hartshorne, *Algebraic Geometry*, III.2.7). The Leray spectral sequence for $\epsilon$,

$$
H^p(W_{\mathrm{Zar}},R^q\epsilon_*F)\Longrightarrow H^{p+q}(W_{\Et},F),
$$

is therefore confined to $0\leq p\leq d$, $0\leq q\leq d+c$, and its abutment vanishes in degrees above $2d+c$. The argument does not use separatedness of $W$.
