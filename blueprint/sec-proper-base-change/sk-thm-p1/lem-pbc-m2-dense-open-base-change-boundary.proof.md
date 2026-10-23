+++
kind = "proof"
of = "lem-pbc-m2-dense-open-base-change-boundary"
+++
*The boundary in $X$.* $X$ is Noetherian and has finitely many irreducible components. For each component $Z$ let $O_Z$ be the open complement of the union of the other components; the generic point of $Z$ lies in $O_Z$, and $O_Z$ is dense in $Z$. Since $U$ is dense it meets every $O_Z$, so $U\cap Z$ is a nonempty open of the irreducible space $Z$ of dimension at most one. Hence $Z\setminus U$ is a finite set of closed points of $Z$, and these are closed in $X$ as $Z$ is closed. The finite union over $Z$ shows that $X\setminus U$ is a finite set of closed points.

*Fibres over boundary points.* Each closed point $x\in X\setminus U$ has residue field $k$, since $X$ is of finite type over the algebraically closed field $k$, so $\operatorname{Spec}\kappa(x)\to X\to\operatorname{Spec}k$ is an isomorphism. Pasting the cartesian square defining the fibre of $a$ over $x$ with the given field-extension square shows that this fibre is isomorphic to $\operatorname{Spec}k'$, a single point. So $a$ is injective on $a^{-1}(X\setminus U)=X'\setminus V$.

*Conclusion.* An injective map onto a subset of a finite set has finite source, so $X'\setminus V$ is finite. For $y\in X'\setminus V$ we have $a^{-1}(\{a(y)\})=\{y\}$, and $\{a(y)\}$ is closed, so $\{y\}$ is closed by continuity. $X'$ is of finite type over $k'$ by base change, so the residue field of the closed point $y$ is $k'$, which is algebraically closed, hence separably closed.
