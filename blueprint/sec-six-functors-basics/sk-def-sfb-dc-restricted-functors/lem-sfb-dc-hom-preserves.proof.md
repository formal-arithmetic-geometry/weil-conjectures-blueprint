+++
kind  = "proof"
of    = "lem-sfb-dc-hom-preserves"
uses = ["lem-sfb-dc-lower-star-preserves", "sk-thm-sfb-qlbar-two-colimit"]
+++
Let first $\Lambda=\underline{\cO}_E$, and use the characterisation of bounded constructible
complexes recalled in the proof of [lem-sfb-dc-lower-star-preserves]. The complex
$\RHom(K,L)$ is derived $\pi_E$-complete, since $L$ is. Since $K$ is bounded constructible,
reduction modulo $\pi_E$ gives

$$
\RHom(K,L)/\pi_E\cong\RHom_{\cO_E/\pi_E}(K/\pi_E,L/\pi_E).
$$

By Deligne's finiteness theorem for the internal $\RHom$ (SGA 4½, *Th. finitude*, 1.6) on the
finite type $k$-scheme $X$, with coefficients in which $p$ is invertible, this is a bounded
complex with constructible cohomology. The cases $\underline E$ and $\underline{\Qlb}$ follow by
inverting $\ell$ and by descending to a finite extension $E$
([sk-thm-sfb-qlbar-two-colimit]), as in
[lem-sfb-dc-lower-star-preserves]; see Bhatt–Scholze, §6.8.
