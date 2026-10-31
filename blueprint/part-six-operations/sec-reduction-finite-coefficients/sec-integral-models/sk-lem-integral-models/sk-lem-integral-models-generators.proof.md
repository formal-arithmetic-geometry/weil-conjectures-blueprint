+++
kind  = "proof"
of    = "det-lem-integral-models-generators"
+++
(1) By [det-cor-coefficient-heart-ii-generation], every $K\in\Dbc(X,E)$ is obtained by finitely
many cones and shifts from objects $a_!L$, $L$ lisse on a locally closed $S$. By
[det-lem-stratified-lattice-trace] there is a finite stratification $S=\coprod_bS_b$, ordered
with open unions ([det-lem-coefficient-heart-common-stratification]), and lattices
$L_{0,b}\subseteq L|_{S_b}$ with $L_{0,b}[1/\ell]=L|_{S_b}$. The filtration of
[det-lem-coefficient-heart-filtration] applied to $L$ on $S$ and pushed forward by the exact
$a_!$ shows that $a_!L$ is an iterated extension of the $a_{b!}(L|_{S_b})$, where
$a_b\colon S_b\hookrightarrow X$ (composites of locally closed immersions are locally closed,
and extension by zero is transitive). Finally $a_{b!}(L|_{S_b})=a_{b!}(L_{0,b}[1/\ell])=(a_{b!}L_{0,b})[1/\ell]$
because $a_{b!}$ is exact and commutes with the filtered colimit defining $[1/\ell]$. Each
extension is a distinguished triangle, so $K$ is built from $\mathcal G_E$ by finitely many
cones and shifts.

(2) By [det-lem-coefficient-finite-descent-objects], $K\cong(K_E)_{\Qlb}$ for some finite $E$ and
$K_E\in\Dbc(X,E)$. Apply (1) to $K_E$; the exact functor $\QbarX\otimes_{E_X}-$ preserves cones
and shifts and sends $E_X\otimes a_!L_0$ to $\QbarX\otimes_{\cO_{E,X}}a_!L_0$.

(3) $L_0$ is locally $\cO_{E,S}^r$; its reductions $L_0/\pi_E^n$ are locally constant sheaves of
finite free $\cO_E/\pi_E^n$-modules, i.e. finitely presented, so they come from the étale site
(\stacks{099Y}) and are constructible; $L_0$ is derived complete (locally finite free over the
complete $\cO_{E,S}$). So $L_0\in\Dbc(S,\cO_E)$ by [sk-prop-integral-criterion], hence
$a_!L_0\in\Dbc(X,\cO_E)$ by [det-lem-integral-models-operations] (3). $L_0$ is flat, so
$a_!L_0\otimes^{\mathbf L}\cO_E/\pi_E^n=a_!(L_0/\pi_E^n)$, which is the extension by zero of a
classical sheaf, again classical and constructible.
