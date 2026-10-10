+++
kind  = "proof"
of    = "prop-asd-internal-adjunction"
+++
For every test complex $Q$ on $S$, the ordinary
derived pullback, tensor, and internal-Hom adjunctions of
[def-weil-derived-pullback-tensor-hom] give

$$
\begin{split}
\operatorname{Hom}_S(Q,Rf_*R\mathcal Hom_A(M,f^\times K))
&\cong\operatorname{Hom}_X(f^*Q\otimes_A^LM,f^\times K)\\
&\cong\operatorname{Hom}_S(Rf_!(f^*Q\otimes_A^LM),K)\\
&\cong\operatorname{Hom}_S(Q\otimes_A^LRf_!M,K)\\
&\cong\operatorname{Hom}_S(Q,R\mathcal Hom_A(Rf_!M,K)).
\end{split}
$$

The second bijection is
[thm-amb-etale-exceptional-adjoint]; the third is the
projection formula of
[lem-amb-proper-coproducts-projection], applied on a
compactification and preceded by exact extension by zero.
These bijections are natural in all three complexes.
Yoneda therefore gives the asserted canonical isomorphism.
It is the map obtained by applying $Rf_!$ to evaluation
and then composing with the counit, since the displayed
bijections transpose precisely those maps.
