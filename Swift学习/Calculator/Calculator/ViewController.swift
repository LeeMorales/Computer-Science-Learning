//
//  ViewController.swift
//  Calculator
//
//  Created by Lee Morales on 2019/5/2.
//  Copyright © 2019 Lee Morales. All rights reserved.
//

import UIKit

class ViewController: UIViewController{
    @IBOutlet weak var display: UILabel!
    
    @IBAction func appendDigit(sender: UIButton) {
        let digit = sender.currentTitle
        print("digit = \(String(describing: digit))")
    }
    
}
