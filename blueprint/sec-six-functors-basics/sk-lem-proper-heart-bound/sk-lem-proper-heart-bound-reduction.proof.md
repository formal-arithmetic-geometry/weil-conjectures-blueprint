+++
kind = "proof"
of = "det-proper-heart-bound-reduction"
+++
*Extensions.* If $0\to M'\to M\to M''\to0$ is exact, the long exact sequence
$R^qp_*M'\to R^qp_*M\to R^qp_*M''$ shows that vanishing for $q>c$ for $M'$ and $M''$ implies it for $M$.
By induction the vanishing passes to finite extensions.

*Strata.* By part (3) of [sk-lem-coefficient-heart], $M$ is a finite extension of sheaves $a_!L$ with
$a\colon S\hookrightarrow X$ locally closed and $L$ a lisse $\Lambda_S$-module. For $\Lambda=\Qlb$, by part
(1) of [sk-thm-sfb-qlbar-two-colimit], $L\cong\overline{\mathbf Q}_{\ell,S}\otimes_{E_S}L_E$ for a lisse
$E_S$-module $L_E$ and some finite $E$; for $\Lambda=E$ put $L_E=L$.

*Lattices.* By [sk-lem-stratified-lattice] there is a finite stratification $S=\coprod_kS_k$ such that
$L_E|_{S_k}$ contains a lisse $\mathcal O_{E,S_k}$-lattice $L_{0,k}$ with $L_{0,k}[1/\ell]=L_E|_{S_k}$; after a
further refinement we may assume it finite free locally. The open–closed exact sequences along the
stratification express $a_!L_E$ as a finite extension of the sheaves $(a_k)_!(L_E|_{S_k})$, with
$a_k\colon S_k\hookrightarrow X$, and similarly for the scalar extension to $\Qlb$ (which is exact, being
flat). Since $(a_k)_!$ is exact and commutes with the filtered colimit inverting $\ell$,
$(a_k)_!(L_E|_{S_k})=((a_k)_!L_{0,k})[1/\ell]$. By the hypotheses and the extension step, $R^qp_*M=0$ for
$q>c$.
