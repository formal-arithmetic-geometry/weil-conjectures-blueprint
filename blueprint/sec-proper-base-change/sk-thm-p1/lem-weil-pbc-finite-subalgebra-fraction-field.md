+++
id = "lem-weil-pbc-finite-subalgebra-fraction-field"
kind = "lemma"
title = "A finite field extension admits a finite algebra model over the power-series polynomial ring"
lean = ["MvPolynomial.exists_finite_subalgebra_fraction_field"]
order = 1774
+++
Let $k$ be a field of characteristic $p>0$, let $n,m\ge0$ and let $A=k[[x_1,\ldots,x_n]][y_1,\ldots,y_m]$ be the polynomial ring in $y_1,\ldots,y_m$ over the formal power series ring $k[[x_1,\ldots,x_n]]$. Then $A$ is an integral domain; let $K=A_{(0)}$ be its fraction field, and let $M/K$ be a finite field extension, i.e. $M$ is a finitely generated $K$-module. Then there is a subring $B\subseteq M$ containing $A$ which is a finitely generated $A$-module and whose fraction field is $M$ (every element of $M$ is $b/s$ with $b,s\in B$, $s\neq0$).
