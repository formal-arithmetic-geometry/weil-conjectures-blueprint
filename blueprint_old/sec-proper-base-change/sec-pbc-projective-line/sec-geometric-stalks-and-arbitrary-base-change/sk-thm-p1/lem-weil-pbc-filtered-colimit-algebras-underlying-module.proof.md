+++
kind = "proof"
of = "lem-weil-pbc-filtered-colimit-algebras-underlying-module"
+++
Step 1 (the underlying set). The forgetful functor from commutative $R$-algebras to commutative rings preserves colimits over connected, in particular filtered, index categories, and the forgetful functor from commutative rings to sets preserves filtered colimits. Hence the underlying set of $A$, with the maps $\iota_i$, is the colimit of the sets $A_i$: every element of $A$ has the form $\iota_i(a)$ with $a\in A_i$, and $\iota_i(a)=\iota_{i'}(a')$ exactly when $a$ and $a'$ become equal at some common later stage.

Step 2 (descent of the compatible maps). Regard the $R$-linear maps $f_i$ as functions; the hypothesis $f_j\circ A(u)=f_i$ says they are compatible. By the universal property of the colimit of sets from step 1 there is a unique function $f:A\to P$ with $f(\iota_i(a))=f_i(a)$ for all $i$ and $a\in A_i$. Well-definedness on representatives is part of this universal property.

Step 3 (linearity). Since $I$ is filtered, any two elements of $A$ can be written as $\iota_i(a)$ and $\iota_i(a')$ at a single stage $i$. Then $f(\iota_i(a)+\iota_i(a'))=f(\iota_i(a+a'))=f_i(a+a')=f_i(a)+f_i(a')$, using additivity of $\iota_i$ and of $f_i$. Similarly, for $r\in R$, $f(r\iota_i(a))=f(\iota_i(ra))=f_i(ra)=rf_i(a)$. So $f$ is $R$-linear.

Step 4 (factorization and uniqueness). By step 2, $f\circ\iota_i=f_i$ for every $i$. Any other $R$-linear map $f'$ with $f'\circ\iota_i=f_i$ agrees with $f$ on every element $\iota_i(a)$, and every element of $A$ is of this form by step 1. Hence $f$ is unique.
