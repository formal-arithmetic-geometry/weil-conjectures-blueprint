+++
kind = "proof"
of = "prop-pc-serre-duality-field-extension"
uses = ["det-thm-picard-duality", "lem-pc-flat-base-change-cohom", "def-pc-base-change", "def-sc-kahler-differentials"]
+++
The morphism $\operatorname{Spec}K\to\operatorname{Spec}k$ is flat, so flat base change
([lem-pc-flat-base-change-cohom]) gives $H^i(C_K,\mathcal F_K)=H^i(C,\mathcal F)\otimes_kK$
for every quasi-coherent $\mathcal F$ on $C$, compatibly with cup products. Kähler
differentials commute with base change ([def-sc-kahler-differentials]), so
$\omega_{C_K/K}=(\omega_{C/k})_K$, and evaluation
$\cL\otimes\cL^{-1}\otimes\omega\to\omega$ commutes with base change. It remains to see
that the trace $t_{C_K}\colon H^1(C_K,\omega_{C_K/K})\to K$ of [det-thm-picard-duality] is
the $K$-linear extension of $t_C$. Both are computed from the residue sequence; the function
field of $C_K$ is $k(C)\otimes_kK$ (localized), the closed points of $C_K$ over a closed
point $x$ of $C$ are the points of $\operatorname{Spec}(\kappa(x)\otimes_kK)$, and Tate's
residue is compatible with extension of the base field: for $\eta\in\Omega^1_{k(C)/k}$,
the sum of the residues of $\eta\otimes1$ at the points over $x$ is $\operatorname{res}_x(\eta)$.
Hence $t_{C_K}(\xi\otimes1)=t_C(\xi)$ for $\xi\in H^1(C,\omega_{C/k})$. The trace pairing
for $\cL_K$ is therefore the $K$-linear extension of the pairing for $\cL$, and so is the
induced isomorphism.
