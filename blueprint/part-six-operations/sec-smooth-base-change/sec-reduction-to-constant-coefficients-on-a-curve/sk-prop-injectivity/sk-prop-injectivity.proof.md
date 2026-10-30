+++
kind = "proof"
of = "sk-prop-injectivity"
+++
Choose $0\to M\to I\to Q\to0$ with $I$ as in the statement. By the long
exact sequences, the rows of the following diagram are exact; the upper
row ends in $0$ because $R^qf_*I=0$ for the injective sheaf $I$, while
$g'^{-1}I$ need not be injective.

$$
\begin{CD}
g^{-1}R^{q-1}f_*I @>>> g^{-1}R^{q-1}f_*Q
@>>> g^{-1}R^qf_*M @>>>0\\
@V{\sim}VV @V{\sim}VV @VVV @VVV\\
R^{q-1}f'_*g'^{-1}I @>>> R^{q-1}f'_*g'^{-1}Q
@>>>R^qf'_*g'^{-1}M @>>>R^qf'_*g'^{-1}I.
\end{CD}
$$

The first two vertical arrows are isomorphisms by
$\mathrm{BC}(g,n,q-1)$. Hence both $g^{-1}R^qf_*M$ and the kernel of
$R^qf'_*g'^{-1}M\to R^qf'_*g'^{-1}I$ are the cokernel of the same map, and
$b_M^q$ is an isomorphism onto this kernel. This proves injectivity and the
last assertion. For $M\subset N$, choose an injective $I$ containing $N$.
Then the cokernels of $b_M^q$ and $b_N^q$ embed compatibly into
$R^qf'_*g'^{-1}I$, and so the first embeds into the second (see [Stacks, Tag 0F03](https://stacks.math.columbia.edu/tag/0F03)).
