+++
kind  = "proof"
of    = "lem-sfb-dc-tensor-preserves"
uses = ["lem-sfb-dc-lower-star-preserves", "sk-thm-sfb-qlbar-two-colimit"]
+++
Let first $\Lambda=\underline{\cO}_E$, and use the characterisation of bounded constructible
complexes recalled in the proof of [lem-sfb-dc-lower-star-preserves]. Since $\cO_E$ is a
discrete valuation ring, bounded complexes of $\cO_E$-modules have finite Tor-amplitude, so
$K\otimes^{\mathrm L}L$ is bounded. For $K$ and $L$ bounded constructible it is derived
$\varpi$-complete (Bhatt–Scholze, §6.8), and its reduction is

$$
(K\otimes^{\mathrm L}L)/\varpi\cong(K/\varpi)\otimes^{\mathrm L}_{\cO_E/\varpi}(L/\varpi).
$$

This is a derived tensor product of bounded constructible étale complexes over the field
$\cO_E/\varpi$, hence bounded with constructible cohomology. The cases $\underline E$ and
$\underline{\Qlb}$ follow by inverting $\ell$ and by descending to a finite extension $E$
([sk-thm-sfb-qlbar-two-colimit]), as in
[lem-sfb-dc-lower-star-preserves].
