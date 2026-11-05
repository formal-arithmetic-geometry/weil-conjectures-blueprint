+++
id = "det-nagata-boundary-divisor-cartier"
kind = "lemma"
title = "The blow-up of the boundary has Cartier boundary and dense interior"
lean = ["AlgebraicGeometry.exists_admissibleBlowup_cartierBoundary_of_coe_support_eq_compl", "AlgebraicGeometry.Scheme.IdealSheafData.isInvertible_comap_blowupMap", "AlgebraicGeometry.Scheme.IdealSheafData.isSchemeTheoreticallyDominant_blowupMap_preimage_compl_support", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.comap_blowupMap", "AlgebraicGeometry.IsAdmissible.isSchemeTheoreticallyDominant_preimage_ι"]
order = 126
uses = ["def-nagata-admissible-blowup", "lemma-nagata-qc-open-complement-ideal-exists"]
+++
Let $T$ be qcqs, $U\subseteq T$ a quasi-compact open, and
$\mathcal I\subseteq\mathcal O_T$ a finite-type quasi-coherent ideal with
$V(\mathcal I)=T\setminus U$ (one exists by
[lemma-nagata-qc-open-complement-ideal-exists]). Let
$b:T'=\operatorname{Bl}_{\mathcal I}(T)\to T$. Then $b$ is a $U$-admissible
blow-up, the extended ideal $\mathcal I\mathcal O_{T'}$ is invertible, so
defines an effective Cartier divisor $E\subseteq T'$, its support is
$T'\setminus b^{-1}(U)$, and $b^{-1}(U)$ is scheme-theoretically dense in
$T'$. Moreover, for every further $b^{-1}(U)$-admissible blow-up
$c:T''\to T'$, the pulled-back ideal $\mathcal I\mathcal O_{T''}$ is again
invertible with support $T''\setminus(bc)^{-1}(U)$, and $(bc)^{-1}(U)$ is
scheme-theoretically dense in $T''$.
