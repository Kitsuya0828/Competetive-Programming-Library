package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strings"
)

func queue() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	queue := list.New()
	var n, k int
	fmt.Fscan(r, &n)
	fmt.Fscan(r, &k)

	var a int
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a)
		queue.PushBack(a)
	}

	for i := 0; i < k; i++ {
		front := queue.Front()
		queue.Remove(front)
		queue.PushBack(0)
	}

	ans := ""
	for e := queue.Front(); e != nil; e = e.Next() {
		ans += fmt.Sprintf("%d ", e.Value)
	}
	ans = strings.TrimRight(ans, " ")

	fmt.Fprintln(w, ans)
}
