+++
kind = "proof"
of = "pur713-lem-shriek-adjunction"
+++
For $K\in D(X_{\Proet},\mathcal O_E/\varpi^n)$ and $L\in D(Y_{\Proet},\mathcal O_E/\varpi^n)$, first apply the supplied proper adjunction and then Lemma “Finite-coefficient derived open-extension adjunction” (`pur713-lem-open-adjunction`):

$$
\begin{aligned}
\operatorname{Hom}\bigl(Rp_{*,\mathcal O_E/\varpi^n}\mathrm D(j_{!,\mathcal O_E/\varpi^n})K,L\bigr)
&\cong\operatorname{Hom}\bigl(\mathrm D(j_{!,\mathcal O_E/\varpi^n})K,Rp^!_{\mathcal O_E/\varpi^n}L\bigr)\\
&\cong\operatorname{Hom}\bigl(K,\mathrm D(j^*_{\mathcal O_E/\varpi^n})Rp^!_{\mathcal O_E/\varpi^n}L\bigr).
\end{aligned}
$$

Each Hom is taken in the category determined by its displayed objects. These bijections are natural in both variables and hence define the composite adjunction, whose unit and counit are the composites of those of the two adjunctions. No constructibility or coefficient-comparison theorem is used.
