+++
kind = "proof"
of = "lem-weil-pbc-finite-projective-prime-local-free"
uses = ["lem-weil-pbc-finite-flat-local-free"]
+++
$M$ is finitely presented: a surjection $A^{\oplus n}\to M$ splits since $M$ is projective, so its kernel $K$ is a direct summand of $A^{\oplus n}$, hence finitely generated, and $A^{\oplus m}\to A^{\oplus n}\to M\to0$ is exact for a surjection $A^{\oplus m}\to K$.

Fix $\mathfrak p$. The localization $M_{\mathfrak p}$ is a finitely generated flat module over the local ring $A_{\mathfrak p}$, hence free [lem-weil-pbc-finite-flat-local-free]; choose a basis $\bar m_1,\dots,\bar m_r$.

For a finitely presented module, a basis of $M_{\mathfrak p}$ lifts to a basis over some localization $A_f$ with $f\notin\mathfrak p$: clear denominators so that the $\bar m_j$ come from elements $m_j\in M$, consider the map $A^{\oplus r}\to M$ they define; its cokernel is finitely generated and its kernel is finitely generated (as $M$ is finitely presented), and both vanish after localizing at $\mathfrak p$, so both are killed by some $f\notin\mathfrak p$. Then $A_f^{\oplus r}\to M_f$ is an isomorphism.
