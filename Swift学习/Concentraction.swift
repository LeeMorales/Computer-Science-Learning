//
//  ViewController.swift
//  concentration
//
//  Created by lee morales on 2019/4/7.
//  Copyright © 2019 lee morales. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBAction func touchCard(_ sender: UIButton){
        flipCard(withEmoji:"🤣", on: sender)
    }
    func flipCard(withEmoji emoji: String, on button: UIButton){
        if button.currentTitle == emoji {
            button.setTitle("", for: UIContrlState.normal)
            button.backgroundColor = #colorLiteral(red: 0.4392156899, green: 0.01176470611, blue: 0.1921568662, alpha: 1)
        } else{
            button.setTitle(emoji, for: UIControlState.normal)
            button.backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
        }
    }
    
}
