+++
id = "sk-thm-rationality"
kind = "theorem"
title = "Rationality of the zeta series"
order = 3228
lean = ["AlgebraicGeometry.Scheme.zetaSeries_rational"]
uses = ["sk-def-roots", "sk-def-zeta", "sk-prop-criterion", "sk-prop-euler", "sk-thm-tracetodeterminant"]
tags = ["sketch"]
+++
Let $X_0$ be a scheme of finite type (quasi-compact and locally of finite
type) over $\Fq$. Then there are $A,B\in\Z[T]$ with $B(0)=1$ and

$$
B(T)\,Z(X_0,T)=A(T)\quad\text{in }\Q[[T]];
$$

in particular $Z(X_0,T)\in\Q(T)\cap(1+T\Z[[T]])$.
