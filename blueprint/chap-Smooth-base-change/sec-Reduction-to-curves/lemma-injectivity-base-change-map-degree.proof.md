+++
kind = "proof"
of = "lemma-injectivity-base-change-map-degree"
order = 674
uses = ["definition-underived-base-change-map"]
+++
We embed $M$ into an injective sheaf and compare the long exact sequences
of the two sides. The induction hypothesis identifies everything in degree
$q-1$, and since the injective sheaf has no higher direct images upstairs,
a diagram chase shows that $b^q_M$ is injective with cokernel inside
$R^qf'_*g'^{-1}I$.

Choose $0\to M\to I\to Q\to0$ with $I$ as in the statement. By the long
exact sequences, the rows of the following diagram are exact. Here the upper
row ends in $0$ because $R^qf_*I=0$ for the injective sheaf $I$, whereas the
lower row does not, because $g'^{-1}I$ need not be injective.

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
$\mathrm{BC}(g,n,q-1)$, applied to $I$ and to $Q$. Exactness of the upper row says that $g^{-1}R^qf_*M$ is the cokernel of the
map $g^{-1}R^{q-1}f_*I\to g^{-1}R^{q-1}f_*Q$, and exactness of the lower row
says that the kernel of $R^qf'_*g'^{-1}M\to R^qf'_*g'^{-1}I$ is the cokernel
of the corresponding map in the lower row. Since the first two vertical
isomorphisms identify these two maps, $b_M^q$ is an isomorphism onto this kernel.
In particular $b^q_M$ is injective, and its cokernel embeds into
$R^qf'_*g'^{-1}I$, which is the last assertion. For $M\subset N$, choose an
injective $I$ containing $N$.
What we have just shown, applied to $M\subset I$ and to $N\subset I$,
embeds the cokernels of $b_M^q$ and $b_N^q$ compatibly into
$R^qf'_*g'^{-1}I$. As in [Stacks, [0F03](https://stacks.math.columbia.edu/tag/0F03)], the map between the cokernels
induced by $M\subset N$ is compatible with these two embeddings and is
therefore injective.
