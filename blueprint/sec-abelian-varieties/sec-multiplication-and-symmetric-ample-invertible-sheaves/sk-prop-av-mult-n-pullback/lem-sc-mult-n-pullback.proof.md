+++
kind  = "proof"
of    = "lem-sc-mult-n-pullback"
uses = ["thm-sc-theorem-of-cube"]
+++
*Reference: Stacks Project, Groupoid Schemes, Lemma 39.9.7,
[Tag 0BFF](https://stacks.math.columbia.edu/tag/0BFF).*

For $n=0$ the map $[0]$ factors through $\Spec k$
([def-sc-mult-n]), and every invertible module on $\Spec k$ is free
of rank one, so $[0]^*\mathcal N\cong\mathcal O_A=\mathcal N^{\otimes0}$.
In the same way $0^*\mathcal L\cong\mathcal O_A$ for every invertible
$\mathcal L$, where $0=[0]$. For $n=1$, $[1]=\mathrm{id}_A$ and there
is nothing to prove.

Pull the relation of [thm-sc-theorem-of-cube] back along
$x\mapsto(x,x,-x)$: since $m_{123}(x,x,-x)=x$,
$m_1(x,x,-x)=m_2(x,x,-x)=x$, $m_3(x,x,-x)=-x$,
$m_{12}(x,x,-x)=2x$, and
$m_{13}(x,x,-x)=m_{23}(x,x,-x)=0$, one gets
$\mathcal L^{\otimes3}\otimes[-1]^*\mathcal L\cong[2]^*\mathcal L$ for every invertible $\mathcal L$, hence
$[2]^*\mathcal N\cong\mathcal N^{\otimes4}$ for symmetric
$\mathcal N$. Next, for $n\geq1$, pull the relation back along
$x\mapsto(x,x,[n-1]x)$: $m_{123}(x,x,[n-1]x)=[n+1]x$,
$m_1=m_2=\mathrm{id}$, $m_3=[n-1]$, $m_{12}=[2]$, and
$m_{13}=m_{23}=[n]$, so

$$
[n+1]^*\mathcal N\otimes\mathcal N^{\otimes2}\otimes
[n-1]^*\mathcal N
\cong[2]^*\mathcal N\otimes[n]^*\mathcal N^{\otimes2}.
$$

We prove $[m]^*\mathcal N\cong\mathcal N^{\otimes m^2}$ by strong
induction on $m$; the cases $m=0,1$ were done above. Let $n\geq1$
and assume the claim for all $m\leq n$. All modules in the last
display are invertible, so we may cancel
$\mathcal N^{\otimes2}\otimes[n-1]^*\mathcal N$ and get

$$
[n+1]^*\mathcal N\cong\mathcal N^{\otimes(4+2n^2-2-(n-1)^2)}
=\mathcal N^{\otimes(n+1)^2},
$$

as required.
