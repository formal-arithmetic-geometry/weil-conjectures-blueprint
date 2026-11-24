+++
id = "prose-06-08"
kind = "hidden"
title = "Duality for the projective line (5)"
order = 553
+++
We build the unit and counit of the adjunction from [$\delta$](@lemma-class-diagonal-projective-line) and from
the [trace](@lemma-cohomology-projective-line-trace). For $M\in D((\mathbf P^1_S)_{\acute{e}t},A)$,
let

$$
\begin{split}
\eta_M:M
&=Rp_{2*}\Delta_*M\\
&\longrightarrow Rp_{2*}\bigl(p_1^*M\href{@definition-tate-twists}{(1)}[2]\bigr)
\xrightarrow{\ \sim\ }p^*Rp_*M\href{@definition-tate-twists}{(1)}[2] .
\end{split}
\tag{6.7}
$$

Here the first arrow is $Rp_{2*}$ applied to $\href{@lemma-class-diagonal-projective-line}{\delta}\otimes p_1^*M$,
where we use the projection formula
$\Delta_*M=\Delta_*A\otimes^{\mathbf L}p_1^*M$, and the second arrow is the [proper base change](@theorem-results-from-etale-theory) isomorphism $p^*Rp_*\simeq Rp_{2*}p_1^*$. For $N\in D(S_{\acute{e}t},A)$,
let

$$
\varepsilon_N:Rp_*\bigl(p^*N\href{@definition-tate-twists}{(1)}[2]\bigr)
\xrightarrow{\ \sim\ }N\otimes_A^{\mathbf L}
Rp_*\href{@definition-tate-twists}{A_{\mathbf P^1_S}(1)}[2]
\xrightarrow{1\otimes \href{@lemma-cohomology-projective-line-trace}{\operatorname{Tr}_p}}N,
\tag{6.8}
$$

where the first arrow is the projection formula. These maps exist for
unbounded complexes by [Stacks, [0F0C](https://stacks.math.columbia.edu/tag/0F0C), [0GL5](https://stacks.math.columbia.edu/tag/0GL5)].
