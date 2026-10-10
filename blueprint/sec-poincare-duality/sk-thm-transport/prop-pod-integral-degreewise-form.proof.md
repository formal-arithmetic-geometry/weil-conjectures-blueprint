+++
kind  = "proof"
of    = "prop-pod-integral-degreewise-form"
+++
By [thm-pod-derived-poincare-duality] at the $\mathcal O_E$-stage, the inverse adjoint $R\Gamma _c(X,K)^\vee \to R\Gamma (X,K^\vee (d))[2d]$ is an isomorphism of derived-complete perfect $\mathcal O_E$-complexes; finite reduction is the derived tensor product $-\otimes ^L_{\mathcal O_E}A_{E,n}$, which is computed levelwise by [def-weil-derived-complete-integral-detailed], so the derived-complete perfectness of the two complexes (the definition of the category at the point of [def-weil-finite-coefficient-point] at the $\mathcal O_E$-stage) gives the levelwise Tor-exact sequences of the statement: for a derived-complete complex $C$ of $\mathcal O_E$-modules of finite Tor-amplitude, the triangle

$$
C\otimes ^L_{\mathcal O_E}K_1 \longrightarrow C\otimes ^L_{\mathcal O_E}K_{n+1} \longrightarrow C\otimes ^L_{\mathcal O_E}K_n \xrightarrow {+1}
$$

of the exact coefficient sequence $0\to A_{E,1}\to A_{E,n+1}\to A_{E,n}\to 0$ yields the Tor-sequence, with the Tor term the $\varpi$-torsion of the $\mathcal O_E$-module and the reduction term the tensor product; the identification of the two terms with $H^i_c(X,K)\otimes _{\mathcal O_E}A_{E,n}$ and $\operatorname {Tor}_1^{\mathcal O_E}(H^{i+1}_c(X,K),A_{E,n})$ is the derived-tensor computation over a principal ideal ring, in which a bounded complex of finite projective $\mathcal O_E$-modules, the perfect representative of the input (the finite-Tor condition of [def-weil-finite-tor-amplitude] and the derived completion of [def-weil-derived-complete-integral-detailed]), replaces the coefficients levelwise. The same argument applied to the second variable $K^\vee (d)$ and to the adjoint map gives the other two sequences. When the cohomology modules are finite projective over $\mathcal O_E$, the Tor terms vanish, so the sequences show that the cohomology of $K_n$ is the reduction of the cohomology of $K$; transporting the perfect derived pairing along these identifications gives $\mathcal O_E$-module perfect pairings levelwise, defining the degreewise maps of the statement.
